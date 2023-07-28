import dns.resolver

def get_name_servers(domain):
    soa_len = 0
    max_attempts = 10

    # First, we find SOA to get the domain for which we will find name servers
    while domain and soa_len <= 1 and max_attempts > 0:
        try:
            # Use dnspython to perform DNS resolution for SOA record
            answers = dns.resolver.resolve(domain, 'SOA')
            SOA = domain
            soa_len = 1
        except dns.resolver.NoAnswer:
            soa_len = 0
            domain = '.'.join(domain.split('.')[1:])
        
        max_attempts -= 1

    # Get NS records
    try:
        # Use dnspython to perform DNS resolution for NS records
        answers = dns.resolver.resolve(domain, 'NS')
        NS = [str(ns) for ns in answers]
    except dns.resolver.NoAnswer:
        NS = []

    # Print NS records each record on a new line
    for ns in NS:
        print(ns)

if __name__ == "__main__":
    # Hardcoded file path containing the list of domains
    filename = "/path/to/your/domains.txt"
    
    with open(filename, 'r') as file:
        domains = file.read().splitlines()
        
    for domain in domains:
        print(f"Domain: {domain}")
        get_name_servers(domain)
        print()
