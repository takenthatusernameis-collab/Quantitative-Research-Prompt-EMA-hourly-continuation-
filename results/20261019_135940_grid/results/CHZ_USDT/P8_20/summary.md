# EMA Hourly Continuation — CHZ/USDT P8_20

**Symbol:** CHZ/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1749 |
| net_profit_factor | 0.3984 |
| net_win_rate | 0.4265 |
| gross_profit_factor | 0.8958 |
| gross_win_rate | 0.4505 |
| sharpe_ratio | -13.0157 |
| sortino_ratio | -7.6951 |
| max_drawdown | 0.9999 |
| cagr | -0.9804 |
| net_avg_win | 8.8762 |
| net_avg_loss | -16.5714 |
| avg_hold_time_bars | 2.8788 |
| exposure | 0.2289 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
