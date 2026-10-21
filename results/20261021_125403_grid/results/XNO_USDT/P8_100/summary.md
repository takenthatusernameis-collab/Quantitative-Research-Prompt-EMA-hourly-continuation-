# EMA Hourly Continuation — XNO/USDT P8_100

**Symbol:** XNO/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 593 |
| net_profit_factor | 0.6549 |
| net_win_rate | 0.4334 |
| gross_profit_factor | 0.7987 |
| gross_win_rate | 0.4334 |
| sharpe_ratio | -3.6112 |
| sortino_ratio | -1.2433 |
| max_drawdown | 0.7668 |
| cagr | -0.4364 |
| net_avg_win | 56.3485 |
| net_avg_loss | -65.8117 |
| avg_hold_time_bars | 21.4519 |
| exposure | 0.5782 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
