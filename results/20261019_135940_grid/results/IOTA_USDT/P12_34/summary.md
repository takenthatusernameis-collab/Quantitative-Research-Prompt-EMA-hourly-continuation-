# EMA Hourly Continuation — IOTA/USDT P12_34

**Symbol:** IOTA/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1344 |
| net_profit_factor | 0.4133 |
| net_win_rate | 0.4390 |
| gross_profit_factor | 0.8527 |
| gross_win_rate | 0.4606 |
| sharpe_ratio | -9.1773 |
| sortino_ratio | -4.7470 |
| max_drawdown | 0.9972 |
| cagr | -0.9023 |
| net_avg_win | 11.9029 |
| net_avg_loss | -22.5380 |
| avg_hold_time_bars | 4.0461 |
| exposure | 0.2472 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
