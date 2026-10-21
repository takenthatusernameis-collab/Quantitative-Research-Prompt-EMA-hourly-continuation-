# EMA Hourly Continuation — AAVE/USDT P8_34

**Symbol:** AAVE/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 679 |
| net_profit_factor | 0.7801 |
| net_win_rate | 0.4978 |
| gross_profit_factor | 1.0075 |
| gross_win_rate | 0.4978 |
| sharpe_ratio | -2.2214 |
| sortino_ratio | -0.8296 |
| max_drawdown | 0.6246 |
| cagr | -0.3170 |
| net_avg_win | 64.6811 |
| net_avg_loss | -82.1822 |
| avg_hold_time_bars | 9.2990 |
| exposure | 0.2870 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
