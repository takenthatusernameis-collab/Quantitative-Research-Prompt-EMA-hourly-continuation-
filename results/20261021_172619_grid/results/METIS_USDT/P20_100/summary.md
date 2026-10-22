# EMA Hourly Continuation — METIS/USDT P20_100

**Symbol:** METIS/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.7240 |
| net_win_rate | 0.4640 |
| gross_profit_factor | 0.8882 |
| gross_win_rate | 0.4640 |
| sharpe_ratio | -2.4080 |
| sortino_ratio | -0.7434 |
| max_drawdown | 0.6301 |
| cagr | -0.2894 |
| net_avg_win | 68.9938 |
| net_avg_loss | -82.4896 |
| avg_hold_time_bars | 18.1907 |
| exposure | 0.3903 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
