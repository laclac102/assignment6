process COUNTING_MATRIX {
    publishDir "results/", mode: "copy"

    input:
        path parsed_clinvar
        path parsed_testregion

    output:
        path '*_counted.csv', emit: couting_matrix

    script:
        """
        counting_matrix.py $parsed_clinvar
        counting_matrix.py $parsed_testregion
        """
}
