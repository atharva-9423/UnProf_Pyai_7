import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

SALES_FILE = "sales_data.csv"
MONTHS     = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
PRODUCTS   = ["Laptop", "Phone", "Tablet"]
COLORS     = ["#3B82F6", "#F97316", "#10B981"]


def load_and_analyze():
    df = pd.read_csv(SALES_FILE)

    laptop_rev = np.array(df[df["product"] == "Laptop"]["revenue"])
    phone_rev  = np.array(df[df["product"] == "Phone"]["revenue"])
    tablet_rev = np.array(df[df["product"] == "Tablet"]["revenue"])

    all_revenue = np.array(df["revenue"])
    all_units   = np.array(df["units_sold"])

    print("=" * 50)
    print("       📊 SALES DATA ANALYSIS — DAY 7")
    print("=" * 50)

    print("\n📌 NumPy Array — All Revenue Values:")
    print(f"  {all_revenue}")

    print("\n📌 Array Slicing — First 3 months revenue:")
    print(f"  {all_revenue[:9]}")

    print("\n📌 Basic Stats (NumPy):")
    print(f"  Total Revenue   : ₹{np.sum(all_revenue):,}")
    print(f"  Average Revenue : ₹{np.mean(all_revenue):,.0f}")
    print(f"  Max Revenue     : ₹{np.max(all_revenue):,}")
    print(f"  Min Revenue     : ₹{np.min(all_revenue):,}")
    print(f"  Std Deviation   : ₹{np.std(all_revenue):,.0f}")

    print("\n📌 Product-wise Total Revenue:")
    for product, rev in zip(PRODUCTS, [laptop_rev, phone_rev, tablet_rev]):
        print(f"  {product:<8}: ₹{np.sum(rev):,}")

    print("=" * 50)

    return laptop_rev, phone_rev, tablet_rev, all_revenue


def create_dashboard(laptop_rev, phone_rev, tablet_rev, all_revenue):
    fig = plt.figure(figsize=(15, 10))
    fig.patch.set_facecolor("#F8FAFC")
    fig.suptitle("📊 UnProf Sales Dashboard — 6 Month Analysis",
                 fontsize=16, fontweight="bold", color="#1E293B", y=0.98)

    gs = gridspec.GridSpec(2, 2, figure=fig, hspace=0.4, wspace=0.3)

    # ── Bar Chart: Monthly Revenue by Product ──────────────────
    ax1 = fig.add_subplot(gs[0, :])
    ax1.set_facecolor("#FFFFFF")
    x = np.arange(len(MONTHS))
    width = 0.25

    ax1.bar(x - width, laptop_rev, width, label="Laptop", color=COLORS[0], alpha=0.9)
    ax1.bar(x,         phone_rev,  width, label="Phone",  color=COLORS[1], alpha=0.9)
    ax1.bar(x + width, tablet_rev, width, label="Tablet", color=COLORS[2], alpha=0.9)

    ax1.set_title("Monthly Revenue by Product", fontweight="bold", color="#1E293B", pad=12)
    ax1.set_xlabel("Month")
    ax1.set_ylabel("Revenue (₹)")
    ax1.set_xticks(x)
    ax1.set_xticklabels(MONTHS)
    ax1.legend()
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"₹{v/1000:.0f}K"))
    ax1.grid(axis="y", alpha=0.3)
    ax1.spines[["top", "right"]].set_visible(False)

    # ── Line Chart: Monthly Revenue Trend per Product ──────────
    ax2 = fig.add_subplot(gs[1, 0])
    ax2.set_facecolor("#FFFFFF")

    ax2.plot(MONTHS, laptop_rev, marker="o", color=COLORS[0], linewidth=2.5, label="Laptop")
    ax2.plot(MONTHS, phone_rev,  marker="s", color=COLORS[1], linewidth=2.5, label="Phone")
    ax2.plot(MONTHS, tablet_rev, marker="^", color=COLORS[2], linewidth=2.5, label="Tablet")

    ax2.set_title("Revenue Trend Over 6 Months", fontweight="bold", color="#1E293B", pad=12)
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Revenue (₹)")
    ax2.legend()
    ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"₹{v/1000:.0f}K"))
    ax2.grid(alpha=0.3)
    ax2.spines[["top", "right"]].set_visible(False)

    # ── Pie Chart: Total Revenue Share by Product ───────────────
    ax3 = fig.add_subplot(gs[1, 1])
    ax3.set_facecolor("#FFFFFF")

    totals = [np.sum(laptop_rev), np.sum(phone_rev), np.sum(tablet_rev)]
    explode = (0.05, 0.05, 0.05)

    wedges, texts, autotexts = ax3.pie(
        totals,
        labels=PRODUCTS,
        colors=COLORS,
        autopct="%1.1f%%",
        explode=explode,
        startangle=140,
        pctdistance=0.82,
    )
    for text in autotexts:
        text.set_fontweight("bold")
        text.set_color("white")

    ax3.set_title("Revenue Share by Product", fontweight="bold", color="#1E293B", pad=12)

    plt.savefig("sales_dashboard.png", dpi=150, bbox_inches="tight",
                facecolor=fig.get_facecolor())
    print("\n✅ Dashboard saved as 'sales_dashboard.png'")
    plt.show()


def main():
    laptop_rev, phone_rev, tablet_rev, all_revenue = load_and_analyze()
    create_dashboard(laptop_rev, phone_rev, tablet_rev, all_revenue)


if __name__ == "__main__":
    main()
