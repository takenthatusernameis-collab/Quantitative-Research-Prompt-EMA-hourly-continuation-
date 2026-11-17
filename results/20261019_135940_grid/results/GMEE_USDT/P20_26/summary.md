# EMA Hourly Continuation — GMEE/USDT P20_26

**Symbol:** GMEE/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1230 |
| net_profit_factor | 0.2665 |
| net_win_rate | 0.3593 |
| gross_profit_factor | 0.5898 |
| gross_win_rate | 0.3846 |
| sharpe_ratio | -13.9017 |
| sortino_ratio | -6.9940 |
| max_drawdown | 0.9999 |
| cagr | -0.9755 |
| net_avg_win | 8.2174 |
| net_avg_loss | -17.2985 |
| avg_hold_time_bars | 2.1772 |
| exposure | 0.1217 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
