import dns.resolver

def get_name_servers(domain):
    soa_len = 0

    # First, we find SOA to get the domain for which we will find name servers
    while domain and soa_len <= 1:
        try:
            answers = dns.resolver.resolve(domain, 'SOA')
            SOA = str(answers[0].mname).rstrip('.')
            soa_len = 1
        except dns.resolver.NoAnswer:
            soa_len = 0
            domain = '.'.join(domain.split('.')[1:])

    # Get NS records
    answers = dns.resolver.resolve(domain, 'NS')
    NS = [str(ns) for ns in answers]

    # Print NS records each record on a new line
    for ns in NS:
        print(ns)

if __name__ == "__main__":
    domain_input = input("Enter the domain: ")
    get_name_servers(domain_input)
