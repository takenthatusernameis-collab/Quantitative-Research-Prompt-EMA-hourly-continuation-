# EMA Hourly Continuation — MOVR/USDT P26_50

**Symbol:** MOVR/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 961 |
| net_profit_factor | 0.4192 |
| net_win_rate | 0.4308 |
| gross_profit_factor | 0.8551 |
| gross_win_rate | 0.4527 |
| sharpe_ratio | -8.1458 |
| sortino_ratio | -3.5594 |
| max_drawdown | 0.9884 |
| cagr | -0.8301 |
| net_avg_win | 17.2274 |
| net_avg_loss | -31.1070 |
| avg_hold_time_bars | 3.7055 |
| exposure | 0.1619 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
