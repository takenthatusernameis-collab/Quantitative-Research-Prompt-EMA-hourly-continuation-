# EMA Hourly Continuation — MTL/USDT P26_34

**Symbol:** MTL/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 417 |
| net_profit_factor | 0.4473 |
| net_win_rate | 0.4317 |
| gross_profit_factor | 0.7845 |
| gross_win_rate | 0.4341 |
| sharpe_ratio | -5.2555 |
| sortino_ratio | -1.5344 |
| max_drawdown | 0.8488 |
| cagr | -0.5191 |
| net_avg_win | 37.8746 |
| net_avg_loss | -64.3036 |
| avg_hold_time_bars | 4.8969 |
| exposure | 0.0924 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
