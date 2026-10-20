# EMA Hourly Continuation — ATH/USDT P55_100

**Symbol:** ATH/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 607 |
| net_profit_factor | 0.5114 |
| net_win_rate | 0.4596 |
| gross_profit_factor | 0.8422 |
| gross_win_rate | 0.4695 |
| sharpe_ratio | -5.0410 |
| sortino_ratio | -1.8156 |
| max_drawdown | 0.8725 |
| cagr | -0.5796 |
| net_avg_win | 32.6455 |
| net_avg_loss | -54.2960 |
| avg_hold_time_bars | 5.1087 |
| exposure | 0.1503 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
