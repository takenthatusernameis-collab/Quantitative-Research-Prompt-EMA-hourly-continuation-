# EMA Hourly Continuation — TFUEL/USDT P21_26

**Symbol:** TFUEL/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1283 |
| net_profit_factor | 0.2345 |
| net_win_rate | 0.3102 |
| gross_profit_factor | 0.7201 |
| gross_win_rate | 0.3819 |
| sharpe_ratio | -17.0518 |
| sortino_ratio | -9.0474 |
| max_drawdown | 1.0000 |
| cagr | -0.9926 |
| net_avg_win | 7.6968 |
| net_avg_loss | -14.7608 |
| avg_hold_time_bars | 2.4131 |
| exposure | 0.1401 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
