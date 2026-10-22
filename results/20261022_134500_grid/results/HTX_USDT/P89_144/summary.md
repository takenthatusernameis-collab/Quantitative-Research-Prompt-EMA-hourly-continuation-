# EMA Hourly Continuation — HTX/USDT P89_144

**Symbol:** HTX/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 560 |
| net_profit_factor | 0.1914 |
| net_win_rate | 0.2696 |
| gross_profit_factor | 0.5593 |
| gross_win_rate | 0.3321 |
| sharpe_ratio | -12.0311 |
| sortino_ratio | -4.3213 |
| max_drawdown | 0.9971 |
| cagr | -0.9008 |
| net_avg_win | 15.6295 |
| net_avg_loss | -30.1483 |
| avg_hold_time_bars | 5.2214 |
| exposure | 0.1323 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
