# EMA Hourly Continuation — CPOOL/USDT P26_89

**Symbol:** CPOOL/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 475 |
| net_profit_factor | 0.7878 |
| net_win_rate | 0.4884 |
| gross_profit_factor | 0.9348 |
| gross_win_rate | 0.4884 |
| sharpe_ratio | -1.5585 |
| sortino_ratio | -0.4847 |
| max_drawdown | 0.4829 |
| cagr | -0.2015 |
| net_avg_win | 69.0714 |
| net_avg_loss | -83.7117 |
| avg_hold_time_bars | 9.7874 |
| exposure | 0.2113 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
