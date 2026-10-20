# EMA Hourly Continuation — OSMO/USDT P89_100

**Symbol:** OSMO/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 551 |
| net_profit_factor | 0.3061 |
| net_win_rate | 0.3920 |
| gross_profit_factor | 0.8647 |
| gross_win_rate | 0.4265 |
| sharpe_ratio | -8.5389 |
| sortino_ratio | -2.8977 |
| max_drawdown | 0.9765 |
| cagr | -0.7745 |
| net_avg_win | 19.9351 |
| net_avg_loss | -41.9955 |
| avg_hold_time_bars | 2.5481 |
| exposure | 0.0638 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
