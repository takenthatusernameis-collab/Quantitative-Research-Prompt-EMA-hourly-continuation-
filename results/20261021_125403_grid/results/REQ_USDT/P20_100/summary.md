# EMA Hourly Continuation — REQ/USDT P20_100

**Symbol:** REQ/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 529 |
| net_profit_factor | 0.6980 |
| net_win_rate | 0.4858 |
| gross_profit_factor | 0.9809 |
| gross_win_rate | 0.4858 |
| sharpe_ratio | -2.9787 |
| sortino_ratio | -0.9791 |
| max_drawdown | 0.6835 |
| cagr | -0.3628 |
| net_avg_win | 60.9426 |
| net_avg_loss | -82.4900 |
| avg_hold_time_bars | 16.4896 |
| exposure | 0.3965 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
