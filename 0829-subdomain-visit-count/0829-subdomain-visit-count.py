class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_count = {}
        for cp_domain in cpdomains:
            count, domain = cp_domain.split(' ')
            count = int(count)

            domains = domain.split('.')
            for i in range(len(domains)):
                subdomain = '.'.join(domains[i:])
                domain_count[subdomain] = domain_count.get(subdomain, 0) + count
        
        res = []
        for domain, count in domain_count.items():
            res.append(f"{count} {domain}")
        
        return res