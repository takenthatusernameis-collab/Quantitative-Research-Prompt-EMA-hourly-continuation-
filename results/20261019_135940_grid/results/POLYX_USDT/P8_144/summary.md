# EMA Hourly Continuation — POLYX/USDT P8_144

**Symbol:** POLYX/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 481 |
| net_profit_factor | 0.6946 |
| net_win_rate | 0.4782 |
| gross_profit_factor | 0.9634 |
| gross_win_rate | 0.4886 |
| sharpe_ratio | -2.6522 |
| sortino_ratio | -0.8172 |
| max_drawdown | 0.6383 |
| cagr | -0.3226 |
| net_avg_win | 61.6848 |
| net_avg_loss | -81.3816 |
| avg_hold_time_bars | 33.2453 |
| exposure | 0.7269 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
