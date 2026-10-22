# EMA Hourly Continuation — LDO/USDT P26_100

**Symbol:** LDO/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 652 |
| net_profit_factor | 0.5800 |
| net_win_rate | 0.4463 |
| gross_profit_factor | 0.8138 |
| gross_win_rate | 0.4509 |
| sharpe_ratio | -4.6091 |
| sortino_ratio | -1.6580 |
| max_drawdown | 0.8635 |
| cagr | -0.5442 |
| net_avg_win | 40.8626 |
| net_avg_loss | -56.7896 |
| avg_hold_time_bars | 12.2592 |
| exposure | 0.3633 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
