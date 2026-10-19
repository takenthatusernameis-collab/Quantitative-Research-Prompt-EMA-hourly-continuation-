# EMA Hourly Continuation — NEAR/USDT P55_89

**Symbol:** NEAR/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 646 |
| net_profit_factor | 0.4576 |
| net_win_rate | 0.4520 |
| gross_profit_factor | 0.8062 |
| gross_win_rate | 0.4582 |
| sharpe_ratio | -5.7328 |
| sortino_ratio | -2.0604 |
| max_drawdown | 0.9226 |
| cagr | -0.6346 |
| net_avg_win | 26.5824 |
| net_avg_loss | -47.9208 |
| avg_hold_time_bars | 3.3359 |
| exposure | 0.0980 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
