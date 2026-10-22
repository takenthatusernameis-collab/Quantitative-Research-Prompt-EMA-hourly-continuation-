# EMA Hourly Continuation — BDX/USDT P20_89

**Symbol:** BDX/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1232 |
| net_profit_factor | 0.3329 |
| net_win_rate | 0.3101 |
| gross_profit_factor | 0.7519 |
| gross_win_rate | 0.3515 |
| sharpe_ratio | -16.8760 |
| sortino_ratio | -8.7405 |
| max_drawdown | 1.0000 |
| cagr | -0.9924 |
| net_avg_win | 13.0620 |
| net_avg_loss | -17.6349 |
| avg_hold_time_bars | 5.6096 |
| exposure | 0.3141 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
