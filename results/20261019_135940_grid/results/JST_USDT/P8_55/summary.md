# EMA Hourly Continuation — JST/USDT P8_55

**Symbol:** JST/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 851 |
| net_profit_factor | 0.3499 |
| net_win_rate | 0.4465 |
| gross_profit_factor | 0.9570 |
| gross_win_rate | 0.4841 |
| sharpe_ratio | -7.7492 |
| sortino_ratio | -3.1514 |
| max_drawdown | 0.9834 |
| cagr | -0.8017 |
| net_avg_win | 13.9231 |
| net_avg_loss | -32.1063 |
| avg_hold_time_bars | 12.7967 |
| exposure | 0.4928 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
