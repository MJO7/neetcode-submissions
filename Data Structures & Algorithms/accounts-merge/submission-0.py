class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            root_a, root_b = find(a), find(b)
            if root_a == root_b:
                return
            if rank[root_a] > rank[root_b]:
                parent[root_b] = root_a
            elif rank[root_a] < rank[root_b]:
                parent[root_a] = root_b
            else:
                parent[root_b] = root_a
                rank[root_a] += 1

        # Step 2: link accounts that share an email.
        email_owner = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_owner:
                    union(i, email_owner[email])
                else:
                    email_owner[email] = i

        # Step 3: group every email under its root account.
        groups = defaultdict(list)
        for email, owner in email_owner.items():
            groups[find(owner)].append(email)

        # Step 4: name first, then sorted emails.
        return [[accounts[root][0]] + sorted(emails)
                for root, emails in groups.items()]