# EMA Hourly Continuation — UMA/USDT P50_100

**Symbol:** UMA/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 414 |
| net_profit_factor | 0.7709 |
| net_win_rate | 0.5193 |
| gross_profit_factor | 1.0755 |
| gross_win_rate | 0.5193 |
| sharpe_ratio | -1.6508 |
| sortino_ratio | -0.4835 |
| max_drawdown | 0.4495 |
| cagr | -0.1984 |
| net_avg_win | 66.6727 |
| net_avg_loss | -93.4436 |
| avg_hold_time_bars | 9.3164 |
| exposure | 0.1753 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
