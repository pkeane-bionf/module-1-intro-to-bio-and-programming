test = list(
  name = "check_cw_data",
  cases = list(
    ottr::TestCase$new(
      name = "check_cw_data_1",
      code = {
        testthat::expect_true(exists('cw'))
      }
    ),
    ottr::TestCase$new(
      name = "check_cw_data_2",
      #hidden = TRUE,
      code = {
        testthat::expect_true(dim(cw)[1] == 2703)
      }
    ),
	ottr::TestCase$new(
      name = "check_cw_data_3",
      #hidden = TRUE,
      code = {
	    testthat::expect_true(dim(cw)[2] == 7)
      }
    )
  )
)


