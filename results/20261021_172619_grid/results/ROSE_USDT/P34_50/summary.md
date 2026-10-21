# EMA Hourly Continuation — ROSE/USDT P34_50

**Symbol:** ROSE/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 271 |
| net_profit_factor | 0.8227 |
| net_win_rate | 0.5277 |
| gross_profit_factor | 1.1209 |
| gross_win_rate | 0.5277 |
| sharpe_ratio | -1.0410 |
| sortino_ratio | -0.2475 |
| max_drawdown | 0.3241 |
| cagr | -0.1079 |
| net_avg_win | 80.8704 |
| net_avg_loss | -109.8179 |
| avg_hold_time_bars | 4.9963 |
| exposure | 0.0615 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
