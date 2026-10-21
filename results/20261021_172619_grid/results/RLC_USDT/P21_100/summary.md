# EMA Hourly Continuation — RLC/USDT P21_100

**Symbol:** RLC/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 504 |
| net_profit_factor | 0.8213 |
| net_win_rate | 0.5159 |
| gross_profit_factor | 1.0550 |
| gross_win_rate | 0.5159 |
| sharpe_ratio | -1.3958 |
| sortino_ratio | -0.4496 |
| max_drawdown | 0.4697 |
| cagr | -0.1886 |
| net_avg_win | 72.1721 |
| net_avg_loss | -93.6390 |
| avg_hold_time_bars | 16.5615 |
| exposure | 0.3794 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
