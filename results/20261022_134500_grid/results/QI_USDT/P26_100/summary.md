# EMA Hourly Continuation — QI/USDT P26_100

**Symbol:** QI/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 594 |
| net_profit_factor | 0.6338 |
| net_win_rate | 0.5017 |
| gross_profit_factor | 1.0618 |
| gross_win_rate | 0.5185 |
| sharpe_ratio | -3.2481 |
| sortino_ratio | -1.1057 |
| max_drawdown | 0.7504 |
| cagr | -0.4167 |
| net_avg_win | 43.1809 |
| net_avg_loss | -68.5855 |
| avg_hold_time_bars | 12.7374 |
| exposure | 0.3424 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
