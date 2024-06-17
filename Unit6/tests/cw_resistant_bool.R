test = list(
  name = "cw_resistant_bool",
  cases = list(
    ottr::TestCase$new(
      name = "cw_resistant_bool_1",
      code = {
        testthat::expect_true(names(cw.pectins.cdta)[8] == "Resistant")
      }
    ),
    ottr::TestCase$new(
      name = "cw_resistant_bool_2",
      #hidden = TRUE,
      code = {
        testthat::expect_true(all(cw.pectins.cdta$Resistant %in% c(TRUE, FALSE)))
      }
    )
  )
)


