class FinanceAgent:
    def calculate_split(self, revenue, artist_percentage=0.5):
        artist_share = revenue * artist_percentage
        label_share = revenue - artist_share
        return {"artist": artist_share, "label": label_share}
