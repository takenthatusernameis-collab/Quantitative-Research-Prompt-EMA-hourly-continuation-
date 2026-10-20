# EMA Hourly Continuation — PUFFER/USDT P12_100

**Symbol:** PUFFER/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 482 |
| net_profit_factor | 0.7934 |
| net_win_rate | 0.5062 |
| gross_profit_factor | 1.0559 |
| gross_win_rate | 0.5124 |
| sharpe_ratio | -1.7842 |
| sortino_ratio | -0.6204 |
| max_drawdown | 0.4732 |
| cagr | -0.2542 |
| net_avg_win | 70.2661 |
| net_avg_loss | -90.7986 |
| avg_hold_time_bars | 22.0560 |
| exposure | 0.6016 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
