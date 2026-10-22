# EMA Hourly Continuation — ERG/USDT P12_100

**Symbol:** ERG/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.6754 |
| net_win_rate | 0.4651 |
| gross_profit_factor | 0.8374 |
| gross_win_rate | 0.4651 |
| sharpe_ratio | -2.5243 |
| sortino_ratio | -0.8034 |
| max_drawdown | 0.6127 |
| cagr | -0.3096 |
| net_avg_win | 54.0712 |
| net_avg_loss | -69.6076 |
| avg_hold_time_bars | 20.5788 |
| exposure | 0.4686 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
