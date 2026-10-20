# EMA Hourly Continuation — MLK/USDT P20_55

**Symbol:** MLK/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1241 |
| net_profit_factor | 0.2720 |
| net_win_rate | 0.2804 |
| gross_profit_factor | 0.5726 |
| gross_win_rate | 0.2949 |
| sharpe_ratio | -15.7011 |
| sortino_ratio | -7.9834 |
| max_drawdown | 1.0000 |
| cagr | -0.9831 |
| net_avg_win | 10.7353 |
| net_avg_loss | -15.3813 |
| avg_hold_time_bars | 4.7421 |
| exposure | 0.2663 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
