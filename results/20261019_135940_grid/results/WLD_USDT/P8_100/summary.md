# EMA Hourly Continuation — WLD/USDT P8_100

**Symbol:** WLD/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 604 |
| net_profit_factor | 0.8237 |
| net_win_rate | 0.5232 |
| gross_profit_factor | 1.1211 |
| gross_win_rate | 0.5265 |
| sharpe_ratio | -1.6014 |
| sortino_ratio | -0.5558 |
| max_drawdown | 0.5776 |
| cagr | -0.2359 |
| net_avg_win | 72.6561 |
| net_avg_loss | -96.7778 |
| avg_hold_time_bars | 24.7086 |
| exposure | 0.6784 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
