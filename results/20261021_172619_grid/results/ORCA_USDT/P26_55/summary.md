# EMA Hourly Continuation — ORCA/USDT P26_55

**Symbol:** ORCA/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 515 |
| net_profit_factor | 0.8220 |
| net_win_rate | 0.5340 |
| gross_profit_factor | 1.1426 |
| gross_win_rate | 0.5340 |
| sharpe_ratio | -1.4459 |
| sortino_ratio | -0.4730 |
| max_drawdown | 0.4709 |
| cagr | -0.1971 |
| net_avg_win | 71.1942 |
| net_avg_loss | -99.2359 |
| avg_hold_time_bars | 7.7961 |
| exposure | 0.1825 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
