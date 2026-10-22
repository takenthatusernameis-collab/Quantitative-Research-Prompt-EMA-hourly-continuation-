# EMA Hourly Continuation — XEC/USDT P12_55

**Symbol:** XEC/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1061 |
| net_profit_factor | 0.4714 |
| net_win_rate | 0.4411 |
| gross_profit_factor | 0.8970 |
| gross_win_rate | 0.4581 |
| sharpe_ratio | -7.7580 |
| sortino_ratio | -3.5229 |
| max_drawdown | 0.9888 |
| cagr | -0.8284 |
| net_avg_win | 18.8320 |
| net_avg_loss | -31.5280 |
| avg_hold_time_bars | 8.6287 |
| exposure | 0.4143 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
