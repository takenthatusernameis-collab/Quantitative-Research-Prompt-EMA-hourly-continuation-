# EMA Hourly Continuation — PEPE/USDT P55_89

**Symbol:** PEPE/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 279 |
| net_profit_factor | 0.7656 |
| net_win_rate | 0.4946 |
| gross_profit_factor | 0.9838 |
| gross_win_rate | 0.4946 |
| sharpe_ratio | -1.4447 |
| sortino_ratio | -0.3457 |
| max_drawdown | 0.3453 |
| cagr | -0.1467 |
| net_avg_win | 77.7543 |
| net_avg_loss | -99.4005 |
| avg_hold_time_bars | 6.3871 |
| exposure | 0.0810 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
