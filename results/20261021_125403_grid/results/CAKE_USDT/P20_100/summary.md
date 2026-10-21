# EMA Hourly Continuation — CAKE/USDT P20_100

**Symbol:** CAKE/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.8281 |
| net_win_rate | 0.5191 |
| gross_profit_factor | 1.0869 |
| gross_win_rate | 0.5212 |
| sharpe_ratio | -1.3381 |
| sortino_ratio | -0.4178 |
| max_drawdown | 0.4410 |
| cagr | -0.1760 |
| net_avg_win | 75.7312 |
| net_avg_loss | -98.6990 |
| avg_hold_time_bars | 19.0148 |
| exposure | 0.4080 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
