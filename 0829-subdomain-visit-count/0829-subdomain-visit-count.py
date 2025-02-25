class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_count = {}
        for cpdomain in cpdomains:
            count, url = cpdomain.split(" ")
            count = int(count)

            domains = url.split(".")
            for i in range(len(domains), 0, -1):
                domain = '.'.join(domains[i-1:])
                domain_count[domain] = domain_count.get(domain, 0) + count

        res = []
        for domain, count in domain_count.items():
            res.append(f"{count} {domain}")

        return res

"""
INITIAL THOUGHTS:
- map of domains to count
- for each url, split into different domains
    - upadte domain count
Time: O(n)
Space: O(n)
"""