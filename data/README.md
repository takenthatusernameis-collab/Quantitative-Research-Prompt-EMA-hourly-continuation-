# Data Module

## Overview

Data loading interface for hourly OHLCV data.

## Supported Formats

- Local CSV files with OHLCV columns: timestamp/close/open/high/low/volume
- Data should be 1-hour bars (document timezone in metadata)

## Usage

Create fixture files in `data/fixtures/` for offline testing. See tests for expected format.
