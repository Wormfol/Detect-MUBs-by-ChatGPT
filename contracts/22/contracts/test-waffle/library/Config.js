// Generated by ReScript, PLEASE EDIT WITH CARE
'use strict';

var Dotenv = require("dotenv");
var Belt_Option = require("rescript/lib/js/belt_Option.js");

Dotenv.config();

var runValueSimulations = Belt_Option.getWithDefault(process.env.RUN_VALUE_SIMULATIONS, "false").toLowerCase() === "true";

var dontRunIntegrationTests = Belt_Option.getWithDefault(process.env.DONT_RUN_INTEGRATION_TESTS, "false").toLowerCase() === "true";

var dontRunUnitTests = Belt_Option.getWithDefault(process.env.DONT_RUN_UNIT_TESTS, "false").toLowerCase() === "true";

var isCI = Belt_Option.getWithDefault(process.env.CI, "false").toLowerCase() === "true";

exports.runValueSimulations = runValueSimulations;
exports.dontRunIntegrationTests = dontRunIntegrationTests;
exports.dontRunUnitTests = dontRunUnitTests;
exports.isCI = isCI;
/*  Not a pure module */