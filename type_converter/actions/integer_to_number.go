package actions

// Code generated by the Komand Go SDK Generator. DO NOT EDIT

// IntegerToNumberInput is the input for IntegerToNumber
type IntegerToNumberInput struct {
	Input int `json:"input"`
}

// IntegerToNumberOutput is the output for IntegerToNumber
type IntegerToNumberOutput struct {
	Output float64 `json:"output"`
}

// IntegerToNumberAction is an action the plugin can take
type IntegerToNumberAction struct{}