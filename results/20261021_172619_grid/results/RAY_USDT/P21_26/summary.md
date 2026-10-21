# EMA Hourly Continuation — RAY/USDT P21_26

**Symbol:** RAY/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 191 |
| net_profit_factor | 0.6803 |
| net_win_rate | 0.4921 |
| gross_profit_factor | 0.9775 |
| gross_win_rate | 0.4921 |
| sharpe_ratio | -1.7347 |
| sortino_ratio | -0.3434 |
| max_drawdown | 0.3545 |
| cagr | -0.1471 |
| net_avg_win | 74.5595 |
| net_avg_loss | -106.2143 |
| avg_hold_time_bars | 4.5916 |
| exposure | 0.0399 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
