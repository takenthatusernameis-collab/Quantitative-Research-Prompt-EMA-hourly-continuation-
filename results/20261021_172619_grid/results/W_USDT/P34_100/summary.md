# EMA Hourly Continuation — W/USDT P34_100

**Symbol:** W/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.8884 |
| net_win_rate | 0.5219 |
| gross_profit_factor | 1.0894 |
| gross_win_rate | 0.5219 |
| sharpe_ratio | -0.7730 |
| sortino_ratio | -0.2377 |
| max_drawdown | 0.3224 |
| cagr | -0.1071 |
| net_avg_win | 82.7516 |
| net_avg_loss | -101.6968 |
| avg_hold_time_bars | 12.8114 |
| exposure | 0.2655 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
