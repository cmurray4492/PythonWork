"""
A list of avaialble functions in this modUle and its purpose.
outlier4sigmafilter - objects in feature that are more then 4 standard deviations out are filtered to np.NaN
outlier3sigmafilter - objects in feature that are more then 3 standard deviations out are filtered to np.NaN

"""
import numpy as np


def outlierIQRCapping(dft, para):
    """
    outlierIQRCapping - is a function to cap outliers at 1.5 
    To visualize a column, or feature us any of the following charts to eyeball the situation
    sns.boxplot(x=df['column' | data=df, x="column");
    sns.histplot(df);
   
    """
    # q25, q50, q75 = np.percentile(dft['column_name'], (25, 50, 75))

    q25, q50, q75 = np.percentile(dft[para], (25, 50, 75))
    iqr = q75 - q25

    min_grade = q25 - (1.5*iqr)
    max_grade = q75 + (1.5*iqr)

    print(f"min_grade: {min_grade}")
    print(f"Q25: {q25}")
    print(f"Q50: {q50}")
    print(f"Q75: {q75}")
    print(f"man_grade: {max_grade}")

    dft[dft[para] < min_grade] # Which values are less than the minimum value
    dft[dft[para]> max_grade] # WHich values are more than th4 maximum value

    mean = np.mean(dft[para])
    stdev = np.std(dft[para])
    print(f"Mean: {mean}")
    print(f"Standard Deviation: {stdev}")

    dft[para] = np.where(dft[para] > max_grade, max_grade, dft[para])
    dft[para] = np.where(dft[para] < min_grade, min_grade, dft[para])   


def outlier4sigmafilter(dft, para):
    """outlier4signmafilter - is a function to look at individual columns
    and if there are any observations past 4 std they are converted to np.NaN

    # dft = target Pandas DataFrame
    # para = column we want to

    pass in the dataframe (renamed dft in function), and the column (renamed para in function)

    when the script is applied a new column is created "filter_" + para, that will contain np.NaN
    which will need to be dealt with latter
    """
    mean = dft[para].mean()
    stdev = dft[para].std()
    lowerfiltervalue = mean - (4 * stdev)
    upperfiltervalue = mean + (4 * stdev)
    print(mean)
    print(stdev)
    print(lowerfiltervalue)
    print(upperfiltervalue)

    dft["filter_" + para] = np.where(
        (dft[para] > lowerfiltervalue) & (dft[para] < upperfiltervalue),
        dft[para],
        np.nan,
    )


def outlier3sigmafilter(dft, para):
    """outlier3signmafilter - is a function to look at individual columns
    and if there are any observations past 3 std they are converted to np.NaN

    # dft = target Pandas DataFrame
    # para = column we want to

    pass in the dataframe (renamed dft in function), and the column (renamed para in function)

    when the script is applied a new column is created "filter_" + para, that will contain np.NaN
    which will need to be dealt with latter
    """
    mean = dft[para].mean()
    stdev = dft[para].std()
    lowerfiltervalue = mean - (3 * stdev)
    upperfiltervalue = mean + (3 * stdev)
    print(mean)
    print(stdev)
    print(lowerfiltervalue)
    print(upperfiltervalue)

    dft["filter_" + para] = np.where(
        (dft[para] > lowerfiltervalue) & (dft[para] < upperfiltervalue),
        dft[para],
        np.nan,
    )
