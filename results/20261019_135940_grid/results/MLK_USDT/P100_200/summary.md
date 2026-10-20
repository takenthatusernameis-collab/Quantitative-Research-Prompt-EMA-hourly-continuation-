# EMA Hourly Continuation — MLK/USDT P100_200

**Symbol:** MLK/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 566 |
| net_profit_factor | 0.3010 |
| net_win_rate | 0.3039 |
| gross_profit_factor | 0.5365 |
| gross_win_rate | 0.3145 |
| sharpe_ratio | -9.2525 |
| sortino_ratio | -3.1397 |
| max_drawdown | 0.9811 |
| cagr | -0.7917 |
| net_avg_win | 24.5518 |
| net_avg_loss | -35.6137 |
| avg_hold_time_bars | 7.2067 |
| exposure | 0.1846 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
