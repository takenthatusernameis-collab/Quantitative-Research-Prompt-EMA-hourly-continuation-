# EMA Hourly Continuation — FLIP/USDT P34_89

**Symbol:** FLIP/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.5987 |
| net_win_rate | 0.4599 |
| gross_profit_factor | 0.8848 |
| gross_win_rate | 0.4688 |
| sharpe_ratio | -3.0057 |
| sortino_ratio | -0.7843 |
| max_drawdown | 0.6070 |
| cagr | -0.3030 |
| net_avg_win | 57.3743 |
| net_avg_loss | -81.6144 |
| avg_hold_time_bars | 15.3472 |
| exposure | 0.2351 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
