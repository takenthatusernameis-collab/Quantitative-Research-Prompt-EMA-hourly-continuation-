# EMA Hourly Continuation — TAO/USDT P26_34

**Symbol:** TAO/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 114 |
| net_profit_factor | 0.5871 |
| net_win_rate | 0.4298 |
| gross_profit_factor | 0.7558 |
| gross_win_rate | 0.4298 |
| sharpe_ratio | -1.7869 |
| sortino_ratio | -0.2707 |
| max_drawdown | 0.2942 |
| cagr | -0.1176 |
| net_avg_win | 78.2700 |
| net_avg_loss | -100.4924 |
| avg_hold_time_bars | 5.2982 |
| exposure | 0.0275 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
