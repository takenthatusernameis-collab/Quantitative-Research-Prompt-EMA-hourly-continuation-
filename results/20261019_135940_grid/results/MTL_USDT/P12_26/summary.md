# EMA Hourly Continuation — MTL/USDT P12_26

**Symbol:** MTL/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1332 |
| net_profit_factor | 0.3770 |
| net_win_rate | 0.4009 |
| gross_profit_factor | 0.8918 |
| gross_win_rate | 0.4347 |
| sharpe_ratio | -12.2601 |
| sortino_ratio | -6.3474 |
| max_drawdown | 0.9997 |
| cagr | -0.9602 |
| net_avg_win | 11.3308 |
| net_avg_loss | -20.1099 |
| avg_hold_time_bars | 3.7875 |
| exposure | 0.2283 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
