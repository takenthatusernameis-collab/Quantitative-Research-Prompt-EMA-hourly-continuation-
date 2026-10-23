# EMA Hourly Continuation — UMA/USDT P89_100

**Symbol:** UMA/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 604 |
| net_profit_factor | 0.2176 |
| net_win_rate | 0.3758 |
| gross_profit_factor | 0.6594 |
| gross_win_rate | 0.4487 |
| sharpe_ratio | -9.4074 |
| sortino_ratio | -3.3573 |
| max_drawdown | 0.9883 |
| cagr | -0.8295 |
| net_avg_win | 12.1051 |
| net_avg_loss | -33.5019 |
| avg_hold_time_bars | 3.0993 |
| exposure | 0.0851 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
