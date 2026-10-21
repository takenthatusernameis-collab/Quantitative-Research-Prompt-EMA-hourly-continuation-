# EMA Hourly Continuation — API3/USDT P89_100

**Symbol:** API3/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 129 |
| net_profit_factor | 0.7307 |
| net_win_rate | 0.5194 |
| gross_profit_factor | 1.0623 |
| gross_win_rate | 0.5194 |
| sharpe_ratio | -1.0532 |
| sortino_ratio | -0.1725 |
| max_drawdown | 0.2005 |
| cagr | -0.0758 |
| net_avg_win | 72.7600 |
| net_avg_loss | -107.6034 |
| avg_hold_time_bars | 5.4806 |
| exposure | 0.0321 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
