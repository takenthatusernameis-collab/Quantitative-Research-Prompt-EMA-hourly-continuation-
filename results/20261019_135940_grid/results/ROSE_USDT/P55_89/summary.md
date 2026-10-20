# EMA Hourly Continuation — ROSE/USDT P55_89

**Symbol:** ROSE/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 693 |
| net_profit_factor | 0.5113 |
| net_win_rate | 0.4517 |
| gross_profit_factor | 0.8695 |
| gross_win_rate | 0.4603 |
| sharpe_ratio | -5.7694 |
| sortino_ratio | -2.1464 |
| max_drawdown | 0.9309 |
| cagr | -0.6477 |
| net_avg_win | 30.9962 |
| net_avg_loss | -49.9311 |
| avg_hold_time_bars | 3.9394 |
| exposure | 0.1241 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
