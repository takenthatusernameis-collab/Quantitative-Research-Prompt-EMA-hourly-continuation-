# EMA Hourly Continuation — ENJ/USDT P50_100

**Symbol:** ENJ/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 626 |
| net_profit_factor | 0.5594 |
| net_win_rate | 0.4760 |
| gross_profit_factor | 0.9669 |
| gross_win_rate | 0.4952 |
| sharpe_ratio | -4.6002 |
| sortino_ratio | -1.6209 |
| max_drawdown | 0.8663 |
| cagr | -0.5423 |
| net_avg_win | 36.6793 |
| net_avg_loss | -59.5675 |
| avg_hold_time_bars | 6.2700 |
| exposure | 0.1776 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
