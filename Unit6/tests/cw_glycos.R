test = list(
  name = "cw_glycos",
  cases = list(
    ottr::TestCase$new(
      name = "cw_glycos_1",
      code = {
        testthat::expect_true(exists('cw.pectins'))
      }
    ),
    ottr::TestCase$new(
      name = "cw_glycos_2",
      #hidden = TRUE,
      code = {
        testthat::expect_true(all(cw.pectins$Antibody %in% pectins))
      }
    ),
	ottr::TestCase$new(
      name = "cw_glycos_3",
      #hidden = TRUE,
      code = {
	    testthat::expect_true(exists('cw.hemi'))
      }
    ),
	ottr::TestCase$new(
      name = "cw_glycos_4",
      #hidden = TRUE,
      code = {
	    testthat::expect_true(all(cw.hemi$Antibody %in% hemicelluloses))
      }
    ),
	ottr::TestCase$new(
      name = "cw_glycos_5",
      #hidden = TRUE,
      code = {
	    testthat::expect_true(exists('cw.glyco'))
      }
    ),
	ottr::TestCase$new(
      name = "cw_glycos_6",
      #hidden = TRUE,
      code = {
	    testthat::expect_true(all(cw.glyco$Antibody %in% glycoproteins))
      }
    )
  )
)