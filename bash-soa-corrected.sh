#!/bin/bash

#Changes made in the corrected version:
#    Replaced the double quotation marks around ${domain} and $SOA with straight quotes, as the original code contains typographic quotation marks, which may cause syntax errors.
#    Changed the single quotes used in the awk command to straight quotes.
    
domain=$1
soa_len=0

# first we find SOA to get the domain for which we will find name servers
until [[ -z "${domain}" ]] || [[ "$soa_len" -gt 1 ]]; do
    SOA=$(dig +short SOA "${domain}")
    soa_len=$(echo $SOA | awk '{ print NF }')

    # Returned SOA is not SOA but CNAME
    if [ "$soa_len" -eq 1 ]; then
        # set returned SOA (CNAME) as the new domain and check again
        domain=$SOA
    # SOA is Empty
    elif [ "$soa_len" -eq 0 ]; then
        # remove one subdomain and check again
        domain=${domain#*.}
    fi
done

# Get NS records
NS=$(dig +short NS "${domain}")

# Print NS records each record on a new line
for ns in $NS; do
    echo $ns
done

