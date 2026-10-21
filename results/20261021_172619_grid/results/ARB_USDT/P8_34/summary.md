# EMA Hourly Continuation — ARB/USDT P8_34

**Symbol:** ARB/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 713 |
| net_profit_factor | 0.7601 |
| net_win_rate | 0.5021 |
| gross_profit_factor | 0.9954 |
| gross_win_rate | 0.5021 |
| sharpe_ratio | -2.1527 |
| sortino_ratio | -0.8248 |
| max_drawdown | 0.6242 |
| cagr | -0.3155 |
| net_avg_win | 54.3396 |
| net_avg_loss | -72.0958 |
| avg_hold_time_bars | 8.4446 |
| exposure | 0.2737 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
