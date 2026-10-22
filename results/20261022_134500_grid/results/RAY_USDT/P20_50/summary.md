# EMA Hourly Continuation — RAY/USDT P20_50

**Symbol:** RAY/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 946 |
| net_profit_factor | 0.5877 |
| net_win_rate | 0.4577 |
| gross_profit_factor | 0.9466 |
| gross_win_rate | 0.4683 |
| sharpe_ratio | -6.3413 |
| sortino_ratio | -2.7251 |
| max_drawdown | 0.9676 |
| cagr | -0.7392 |
| net_avg_win | 31.7914 |
| net_avg_loss | -45.6597 |
| avg_hold_time_bars | 5.0793 |
| exposure | 0.2184 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
