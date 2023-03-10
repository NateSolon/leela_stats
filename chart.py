import matplotlib.pyplot as plt


def plot_length(df):
    plt.style.use("ggplot")
    plt.rcParams["figure.figsize"] = (20, 5)
    ax = df.length.hist(bins=20, color="red")
    ax.set_title("Length")
    ax.set_xlabel("Moves")
    ax.set_ylabel("Games")
    fig = ax.get_figure()
    fig.savefig("length.png")

def plot_results(df):
    results = df.result.value_counts()
    total = results.sum()

    w_pct = (results[1]/total * 100).round()
    b_pct = (results[0]/total * 100).round()
    d_pct = (results[0.5]/total * 100).round()

    plt.style.use("default")
    plt.rcParams["figure.figsize"] = (20, 5)

    fig, ax = plt.subplots()
    ax.set_title("Results")

    W = plt.barh(0, [w_pct], color="whitesmoke", label="test")
    ax.bar_label(W, label_type="center", color="black", fmt='%.0f%%')
    D = plt.barh(0, [d_pct], left=[w_pct], color="gray")
    B = plt.barh(0, [b_pct], left=[w_pct + d_pct], color="black")
    ax.bar_label(B, label_type="center", color="white", fmt='%.0f%%')

    plt.axis("off")
    fig.savefig("results.png")