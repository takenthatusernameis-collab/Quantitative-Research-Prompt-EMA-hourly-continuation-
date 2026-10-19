# EMA Hourly Continuation — LDO/USDT P26_50

**Symbol:** LDO/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1024 |
| net_profit_factor | 0.4327 |
| net_win_rate | 0.4326 |
| gross_profit_factor | 0.7832 |
| gross_win_rate | 0.4492 |
| sharpe_ratio | -8.3325 |
| sortino_ratio | -3.7526 |
| max_drawdown | 0.9910 |
| cagr | -0.8465 |
| net_avg_win | 17.0609 |
| net_avg_loss | -30.0648 |
| avg_hold_time_bars | 3.4287 |
| exposure | 0.1596 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
