# EMA Hourly Continuation — CETUS/USDT P20_55

**Symbol:** CETUS/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 954 |
| net_profit_factor | 0.6182 |
| net_win_rate | 0.4497 |
| gross_profit_factor | 0.9624 |
| gross_win_rate | 0.4602 |
| sharpe_ratio | -6.3095 |
| sortino_ratio | -2.7276 |
| max_drawdown | 0.9671 |
| cagr | -0.7338 |
| net_avg_win | 36.4112 |
| net_avg_loss | -48.1249 |
| avg_hold_time_bars | 5.6143 |
| exposure | 0.2424 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
