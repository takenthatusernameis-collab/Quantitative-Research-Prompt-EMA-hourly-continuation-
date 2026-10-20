# EMA Hourly Continuation — FLOW/USDT P21_144

**Symbol:** FLOW/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 481 |
| net_profit_factor | 0.5854 |
| net_win_rate | 0.4595 |
| gross_profit_factor | 0.8990 |
| gross_win_rate | 0.4678 |
| sharpe_ratio | -3.7610 |
| sortino_ratio | -1.1581 |
| max_drawdown | 0.7569 |
| cagr | -0.4265 |
| net_avg_win | 48.0827 |
| net_avg_loss | -69.8112 |
| avg_hold_time_bars | 25.4719 |
| exposure | 0.5569 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
