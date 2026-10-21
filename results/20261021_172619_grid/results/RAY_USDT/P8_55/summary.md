# EMA Hourly Continuation — RAY/USDT P8_55

**Symbol:** RAY/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 704 |
| net_profit_factor | 0.8246 |
| net_win_rate | 0.4986 |
| gross_profit_factor | 1.0093 |
| gross_win_rate | 0.4986 |
| sharpe_ratio | -1.8134 |
| sortino_ratio | -0.6881 |
| max_drawdown | 0.6170 |
| cagr | -0.2734 |
| net_avg_win | 73.8873 |
| net_avg_loss | -89.0949 |
| avg_hold_time_bars | 13.9190 |
| exposure | 0.4454 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
