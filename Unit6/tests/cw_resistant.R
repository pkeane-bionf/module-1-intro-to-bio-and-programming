test = list(
  name = "cw_resistant",
  cases = list(
    ottr::TestCase$new(
      name = "cw_resistant_1",
      code = {
        testthat::expect_true(length(resistant) == 2)
      }
    ),
    ottr::TestCase$new(
      name = "cw_resistant_2",
      #hidden = TRUE,
      code = {
        testthat::expect_true(resistant[1] == "Sarpo Shona")
      }
    ),
	ottr::TestCase$new(
      name = "cw_resistant_3",
      #hidden = TRUE,
      code = {
	    testthat::expect_true(resistant[2] == "Sarpo Mira")
      }
    )
  )
)