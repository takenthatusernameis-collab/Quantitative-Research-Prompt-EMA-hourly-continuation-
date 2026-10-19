# EMA Hourly Continuation — POL/USDT P20_100

**Symbol:** POL/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 633 |
| net_profit_factor | 0.5414 |
| net_win_rate | 0.4787 |
| gross_profit_factor | 0.8802 |
| gross_win_rate | 0.4866 |
| sharpe_ratio | -4.1120 |
| sortino_ratio | -1.4441 |
| max_drawdown | 0.8451 |
| cagr | -0.5071 |
| net_avg_win | 32.3651 |
| net_avg_loss | -54.8917 |
| avg_hold_time_bars | 16.8341 |
| exposure | 0.4844 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
