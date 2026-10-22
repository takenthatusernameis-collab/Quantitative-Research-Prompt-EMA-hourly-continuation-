# EMA Hourly Continuation — EIGEN/USDT P26_50

**Symbol:** EIGEN/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 775 |
| net_profit_factor | 0.5720 |
| net_win_rate | 0.4800 |
| gross_profit_factor | 0.9329 |
| gross_win_rate | 0.4865 |
| sharpe_ratio | -5.4751 |
| sortino_ratio | -2.3731 |
| max_drawdown | 0.9057 |
| cagr | -0.6822 |
| net_avg_win | 32.5006 |
| net_avg_loss | -52.4522 |
| avg_hold_time_bars | 3.5665 |
| exposure | 0.1538 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
