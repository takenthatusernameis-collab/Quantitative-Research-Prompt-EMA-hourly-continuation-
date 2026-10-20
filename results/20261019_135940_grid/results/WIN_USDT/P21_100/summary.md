# EMA Hourly Continuation — WIN/USDT P21_100

**Symbol:** WIN/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 619 |
| net_profit_factor | 0.4557 |
| net_win_rate | 0.4378 |
| gross_profit_factor | 0.8153 |
| gross_win_rate | 0.4540 |
| sharpe_ratio | -6.0826 |
| sortino_ratio | -2.1239 |
| max_drawdown | 0.9316 |
| cagr | -0.6551 |
| net_avg_win | 28.7632 |
| net_avg_loss | -49.1515 |
| avg_hold_time_bars | 14.6834 |
| exposure | 0.4131 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
