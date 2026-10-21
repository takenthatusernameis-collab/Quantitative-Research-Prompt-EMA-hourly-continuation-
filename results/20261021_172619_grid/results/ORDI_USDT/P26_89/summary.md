# EMA Hourly Continuation — ORDI/USDT P26_89

**Symbol:** ORDI/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.7350 |
| net_win_rate | 0.4741 |
| gross_profit_factor | 0.9103 |
| gross_win_rate | 0.4741 |
| sharpe_ratio | -2.2254 |
| sortino_ratio | -0.6969 |
| max_drawdown | 0.5798 |
| cagr | -0.2740 |
| net_avg_win | 66.9076 |
| net_avg_loss | -82.0735 |
| avg_hold_time_bars | 11.9855 |
| exposure | 0.2631 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
