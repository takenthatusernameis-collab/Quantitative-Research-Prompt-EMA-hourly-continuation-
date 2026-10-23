# EMA Hourly Continuation — LUNA/USDT P55_89

**Symbol:** LUNA/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 772 |
| net_profit_factor | 0.3571 |
| net_win_rate | 0.4249 |
| gross_profit_factor | 0.8093 |
| gross_win_rate | 0.4521 |
| sharpe_ratio | -8.5336 |
| sortino_ratio | -3.3603 |
| max_drawdown | 0.9871 |
| cagr | -0.8212 |
| net_avg_win | 16.7124 |
| net_avg_loss | -34.5700 |
| avg_hold_time_bars | 3.6360 |
| exposure | 0.1276 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
