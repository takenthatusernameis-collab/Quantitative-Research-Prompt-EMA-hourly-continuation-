# EMA Hourly Continuation — ORBS/USDT P20_100

**Symbol:** ORBS/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 718 |
| net_profit_factor | 0.6224 |
| net_win_rate | 0.4526 |
| gross_profit_factor | 0.9878 |
| gross_win_rate | 0.4610 |
| sharpe_ratio | -5.4429 |
| sortino_ratio | -2.0545 |
| max_drawdown | 0.9251 |
| cagr | -0.6288 |
| net_avg_win | 46.5051 |
| net_avg_loss | -61.7912 |
| avg_hold_time_bars | 14.2354 |
| exposure | 0.4646 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
