# 🐍 **Python Pandas Data Manipulation Toolkit**
### *Mastering Data Wrangling, Merging, and Statistical Aggregation*

---

## 📝 **PROJECT OVERVIEW**
This repository serves as a practical guide and toolkit for performing high-level data manipulation using the **Pandas** library in Python. It covers the full lifecycle of data handling—from creating DataFrames and importing external CSV files to executing complex relational joins and generating business intelligence reports through pivot tables.

---

## 🛠️ **CORE TECHNICAL FEATURES**
The script (`DataFrame.py`) is structured into specialized modules to demonstrate key data science workflows:

* 🖇️ **Relational Joins:** Implementation of SQL-like joins (**Inner, Outer, Left, Right**) to merge disparate datasets using unique identifiers.
* 📊 **Statistical Aggregations:** Automated computation of Mean, Median, Standard Deviation, Min/Max, and Sum across large datasets (2000+ records).
* 📑 **Advanced Data Reshaping:** Utilization of **Pivot Tables** and **Crosstabs** to summarize complex relationships between variables (e.g., Department vs. Annual Salary).
* 📈 **Visual Reporting:** Integration with **Matplotlib** to generate and auto-save high-resolution graphical reports (Line charts, PNG exports).



---

## 📊 **DATASET CAPABILITIES**
The toolkit is designed to process:
- **Custom DataFrames:** Manually constructed dictionaries and lists for testing logic.
- **External Data:** Automated ingestion of `IT_Employees_Info_2000.csv` for real-world statistical testing.

---

## ⚙️ **TECHNICAL STACK**
* **Language:** `Python 3.x`
* **Libraries:** * `Pandas`: The primary engine for data wrangling and analysis.
    * `Matplotlib`: For generating statistical visual representations.
* **Key Functions Used:** `pd.merge()`, `pd.pivot_table()`, `df.groupby()`, `pd.crosstab()`, `plt.savefig()`.

---

## 📈 **EXECUTIVE SUMMARY OF FUNCTIONS**
| Feature | Description |
| :--- | :--- |
| **Data Merging** | Seamlessly combining tables using `on='ID'` to create unified datasets. |
| **Aggregation** | Batch processing of `numeric_only` statistics for rapid EDA. |
| **Visualization** | Automated saving of charts using `plt.savefig()` for reporting. |

---

## 🚀 **HOW TO RUN**
1. Ensure you have Python installed.
2. Install the required library:
   ```bash
   pip install pandas matplotlib
3. Place your dataset (IT_Employees_Info_2000.csv) in the root directory.
4. Execute the script:
   python DataFrame.py

### Final Commit Instruction**
To keep your GitHub professional, use these commands to upload your files:

**For the script:**
> `git commit -m "feat: add comprehensive pandas data manipulation and aggregation scripts"`

**For the dataset (if you have it):**
> `git commit -m "data: add IT employee dataset for statistical analysis"`

**This is a great project to post because it shows you can handle "dirty" data and transform it into a "clean" format ready for business decisions.**
Execute the script:
