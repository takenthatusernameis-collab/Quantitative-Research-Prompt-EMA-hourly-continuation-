# EMA Hourly Continuation — LUNC/USDT P34_55

**Symbol:** LUNC/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 954 |
| net_profit_factor | 0.2900 |
| net_win_rate | 0.4046 |
| gross_profit_factor | 0.7252 |
| gross_win_rate | 0.4340 |
| sharpe_ratio | -10.5584 |
| sortino_ratio | -4.6582 |
| max_drawdown | 0.9976 |
| cagr | -0.9067 |
| net_avg_win | 10.5564 |
| net_avg_loss | -24.7340 |
| avg_hold_time_bars | 2.9853 |
| exposure | 0.1295 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
