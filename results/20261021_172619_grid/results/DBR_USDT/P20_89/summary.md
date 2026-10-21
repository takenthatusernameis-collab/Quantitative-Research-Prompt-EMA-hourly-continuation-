# EMA Hourly Continuation — DBR/USDT P20_89

**Symbol:** DBR/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.6428 |
| net_win_rate | 0.4695 |
| gross_profit_factor | 0.8573 |
| gross_win_rate | 0.4695 |
| sharpe_ratio | -2.8799 |
| sortino_ratio | -0.8912 |
| max_drawdown | 0.5878 |
| cagr | -0.3352 |
| net_avg_win | 56.8765 |
| net_avg_loss | -78.3065 |
| avg_hold_time_bars | 17.6472 |
| exposure | 0.3783 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
