import dns.resolver

def get_name_servers(domain):
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = ['8.8.8.8', '8.8.4.4']  # Replace with your preferred DNS servers
    soa_len = 0

    # Rest of the code remains the same
    # ...
