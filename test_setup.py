class FakeStreamlit:
    def title(self, text): print(f"\n📘 [Title] {text}")
    def header(self, text): print(f"\n📌 [Header] {text}")
    def metric(self, label, value): print(f"📊 {label}: {value}")
    def error(self, msg): print(f"❌ ERROR: {msg}")
    def warning(self, msg): print(f"⚠️ WARNING: {msg}")
    def plotly_chart(self, chart): print("📈 [Plotly Chart Rendered]")
    def dataframe(self, df): print("🧾 [DataFrame Displayed] Sample:\n", df.head())
    def write(self, text): print(text)

import builtins
builtins.st = FakeStreamlit()
print("✅ Test mode: FakeStreamlit loaded.")