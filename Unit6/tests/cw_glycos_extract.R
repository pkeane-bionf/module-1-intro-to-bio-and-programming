test = list(
  name = "cw_glycos_extract",
  cases = list(
    ottr::TestCase$new(
      name = "cw_glycos_extract_1",
      code = {
        testthat::expect_true(exists('cw.pectins.cdta'))
      }
    ),
    ottr::TestCase$new(
      name = "cw_glycos_extract_2",
      #hidden = TRUE,
      code = {
        testthat::expect_true(all(cw.pectins.cdta$Extraction =="CDTA"))
      }
    ),
	ottr::TestCase$new(
      name = "cw_glycos_extract_3",
      #hidden = TRUE,
      code = {
	    testthat::expect_true(exists('cw.hemi.naoh'))
      }
    ),
	ottr::TestCase$new(
      name = "cw_glycos_extract_4",
      #hidden = TRUE,
      code = {
	    testthat::expect_true(all(cw.hemi.naoh$Extraction == "NaOH"))
      }
    ),
	ottr::TestCase$new(
      name = "cw_glycos_extract_5",
      #hidden = TRUE,
      code = {
	    testthat::expect_true(exists('cw.glyco.naoh'))
      }
    ),
	ottr::TestCase$new(
      name = "cw_glycos_extract_6",
      #hidden = TRUE,
      code = {
	    testthat::expect_true(all(cw.glyco.naoh$Extraction == "NaOH"))
      }
    )
  )
)