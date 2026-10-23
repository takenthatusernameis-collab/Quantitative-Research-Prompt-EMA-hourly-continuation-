# EMA Hourly Continuation — ATH/USDT P89_200

**Symbol:** ATH/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.5537 |
| net_win_rate | 0.4557 |
| gross_profit_factor | 0.8362 |
| gross_win_rate | 0.4581 |
| sharpe_ratio | -3.7685 |
| sortino_ratio | -1.1015 |
| max_drawdown | 0.7217 |
| cagr | -0.4127 |
| net_avg_win | 47.9037 |
| net_avg_loss | -72.4268 |
| avg_hold_time_bars | 10.2315 |
| exposure | 0.2013 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
