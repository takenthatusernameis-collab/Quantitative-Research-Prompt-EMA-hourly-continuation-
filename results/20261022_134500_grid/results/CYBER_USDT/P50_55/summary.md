# EMA Hourly Continuation — CYBER/USDT P50_55

**Symbol:** CYBER/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 786 |
| net_profit_factor | 0.2744 |
| net_win_rate | 0.4020 |
| gross_profit_factor | 0.9285 |
| gross_win_rate | 0.4746 |
| sharpe_ratio | -10.4602 |
| sortino_ratio | -4.2319 |
| max_drawdown | 0.9968 |
| cagr | -0.8969 |
| net_avg_win | 11.9288 |
| net_avg_loss | -29.2260 |
| avg_hold_time_bars | 2.6323 |
| exposure | 0.0940 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
