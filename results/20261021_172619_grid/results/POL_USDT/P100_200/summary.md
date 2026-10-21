# EMA Hourly Continuation — POL/USDT P100_200

**Symbol:** POL/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 252 |
| net_profit_factor | 0.6637 |
| net_win_rate | 0.4722 |
| gross_profit_factor | 0.8732 |
| gross_win_rate | 0.4722 |
| sharpe_ratio | -1.9189 |
| sortino_ratio | -0.4346 |
| max_drawdown | 0.4177 |
| cagr | -0.1813 |
| net_avg_win | 65.4881 |
| net_avg_loss | -88.2857 |
| avg_hold_time_bars | 13.9087 |
| exposure | 0.1593 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
