# EMA Hourly Continuation — CRV/USDT P20_50

**Symbol:** CRV/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 474 |
| net_profit_factor | 0.8190 |
| net_win_rate | 0.5148 |
| gross_profit_factor | 1.0619 |
| gross_win_rate | 0.5148 |
| sharpe_ratio | -1.3993 |
| sortino_ratio | -0.4384 |
| max_drawdown | 0.4335 |
| cagr | -0.1830 |
| net_avg_win | 73.8098 |
| net_avg_loss | -95.6058 |
| avg_hold_time_bars | 7.1624 |
| exposure | 0.1543 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
