import matplotlib.pyplot as plt


if __name__ == "__main__":
    values = [1, 2, 3, 4, 5]
    squares = [1, 4, 9, 16, 25]

    plt.style.use('seaborn')
    
    fig, ax = plt.subplots()
    ax.plot(values, squares, linewidth=2)

    ax.set_title("Square numbers", fontsize=24)
    ax.set_xlabel("Value", fontsize=14)
    ax.set_ylabel("Square of Value", fontsize=14)

    ax.tick_params(axis='both', labelsize=14)

    plt.show()
