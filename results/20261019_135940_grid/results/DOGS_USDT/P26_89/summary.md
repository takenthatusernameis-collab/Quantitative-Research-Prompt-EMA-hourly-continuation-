# EMA Hourly Continuation — DOGS/USDT P26_89

**Symbol:** DOGS/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 643 |
| net_profit_factor | 0.6381 |
| net_win_rate | 0.4914 |
| gross_profit_factor | 0.9255 |
| gross_win_rate | 0.4930 |
| sharpe_ratio | -3.6700 |
| sortino_ratio | -1.4329 |
| max_drawdown | 0.7622 |
| cagr | -0.4853 |
| net_avg_win | 42.4352 |
| net_avg_loss | -64.2646 |
| avg_hold_time_bars | 9.4230 |
| exposure | 0.3214 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
