# EMA Hourly Continuation — PEOPLE/USDT P8_50

**Symbol:** PEOPLE/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 653 |
| net_profit_factor | 0.6795 |
| net_win_rate | 0.4472 |
| gross_profit_factor | 0.8213 |
| gross_win_rate | 0.4472 |
| sharpe_ratio | -3.3934 |
| sortino_ratio | -1.2260 |
| max_drawdown | 0.7665 |
| cagr | -0.4316 |
| net_avg_win | 55.1336 |
| net_avg_loss | -65.6334 |
| avg_hold_time_bars | 16.2818 |
| exposure | 0.4811 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
