# EMA Hourly Continuation — LQTY/USDT P50_144

**Symbol:** LQTY/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 518 |
| net_profit_factor | 0.6235 |
| net_win_rate | 0.4672 |
| gross_profit_factor | 0.9237 |
| gross_win_rate | 0.4788 |
| sharpe_ratio | -3.4248 |
| sortino_ratio | -1.0993 |
| max_drawdown | 0.7299 |
| cagr | -0.4027 |
| net_avg_win | 49.7847 |
| net_avg_loss | -70.0089 |
| avg_hold_time_bars | 11.9421 |
| exposure | 0.2799 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
