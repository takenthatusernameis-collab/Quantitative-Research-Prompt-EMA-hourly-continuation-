# EMA Hourly Continuation — ANKR/USDT P8_89

**Symbol:** ANKR/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 507 |
| net_profit_factor | 0.8218 |
| net_win_rate | 0.5089 |
| gross_profit_factor | 1.0440 |
| gross_win_rate | 0.5089 |
| sharpe_ratio | -1.5280 |
| sortino_ratio | -0.4926 |
| max_drawdown | 0.4886 |
| cagr | -0.2044 |
| net_avg_win | 78.0947 |
| net_avg_loss | -98.4647 |
| avg_hold_time_bars | 28.5325 |
| exposure | 0.6575 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
