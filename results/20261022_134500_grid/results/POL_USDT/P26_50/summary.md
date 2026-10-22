# EMA Hourly Continuation — POL/USDT P26_50

**Symbol:** POL/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1010 |
| net_profit_factor | 0.3007 |
| net_win_rate | 0.4139 |
| gross_profit_factor | 0.6840 |
| gross_win_rate | 0.4386 |
| sharpe_ratio | -9.8233 |
| sortino_ratio | -4.4465 |
| max_drawdown | 0.9962 |
| cagr | -0.8917 |
| net_avg_win | 10.2482 |
| net_avg_loss | -24.0644 |
| avg_hold_time_bars | 3.8000 |
| exposure | 0.1745 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
