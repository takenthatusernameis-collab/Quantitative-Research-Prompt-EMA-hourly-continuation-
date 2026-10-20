# EMA Hourly Continuation — ELON/USDT P20_50

**Symbol:** ELON/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 961 |
| net_profit_factor | 0.3907 |
| net_win_rate | 0.4204 |
| gross_profit_factor | 0.7328 |
| gross_win_rate | 0.4277 |
| sharpe_ratio | -8.5798 |
| sortino_ratio | -3.7854 |
| max_drawdown | 0.9901 |
| cagr | -0.8405 |
| net_avg_win | 15.7128 |
| net_avg_loss | -29.1713 |
| avg_hold_time_bars | 4.6556 |
| exposure | 0.2034 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
