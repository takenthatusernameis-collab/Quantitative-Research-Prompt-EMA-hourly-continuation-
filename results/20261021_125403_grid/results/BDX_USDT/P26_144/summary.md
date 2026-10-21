# EMA Hourly Continuation — BDX/USDT P26_144

**Symbol:** BDX/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 442 |
| net_profit_factor | 0.5275 |
| net_win_rate | 0.4367 |
| gross_profit_factor | 0.8177 |
| gross_win_rate | 0.4389 |
| sharpe_ratio | -4.4728 |
| sortino_ratio | -1.3432 |
| max_drawdown | 0.8022 |
| cagr | -0.4650 |
| net_avg_win | 45.8143 |
| net_avg_loss | -67.3212 |
| avg_hold_time_bars | 13.7059 |
| exposure | 0.2754 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
