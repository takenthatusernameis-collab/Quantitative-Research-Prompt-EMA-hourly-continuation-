# EMA Hourly Continuation — PENDLE/USDT P12_55

**Symbol:** PENDLE/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 642 |
| net_profit_factor | 0.7363 |
| net_win_rate | 0.4766 |
| gross_profit_factor | 0.9013 |
| gross_win_rate | 0.4766 |
| sharpe_ratio | -2.4052 |
| sortino_ratio | -0.8684 |
| max_drawdown | 0.6403 |
| cagr | -0.3294 |
| net_avg_win | 57.8053 |
| net_avg_loss | -71.4950 |
| avg_hold_time_bars | 11.5280 |
| exposure | 0.3364 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
