# EMA Hourly Continuation — INJ/USDT P34_89

**Symbol:** INJ/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 419 |
| net_profit_factor | 0.8024 |
| net_win_rate | 0.4988 |
| gross_profit_factor | 0.9940 |
| gross_win_rate | 0.4988 |
| sharpe_ratio | -1.4384 |
| sortino_ratio | -0.4218 |
| max_drawdown | 0.3955 |
| cagr | -0.1772 |
| net_avg_win | 75.2183 |
| net_avg_loss | -93.2986 |
| avg_hold_time_bars | 10.6730 |
| exposure | 0.2033 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
