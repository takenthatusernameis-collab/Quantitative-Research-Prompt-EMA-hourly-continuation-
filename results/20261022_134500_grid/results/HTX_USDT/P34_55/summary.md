# EMA Hourly Continuation — HTX/USDT P34_55

**Symbol:** HTX/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1006 |
| net_profit_factor | 0.1050 |
| net_win_rate | 0.2256 |
| gross_profit_factor | 0.4491 |
| gross_win_rate | 0.3221 |
| sharpe_ratio | -18.1689 |
| sortino_ratio | -9.0617 |
| max_drawdown | 1.0000 |
| cagr | -0.9929 |
| net_avg_win | 5.1694 |
| net_avg_loss | -14.3433 |
| avg_hold_time_bars | 3.6660 |
| exposure | 0.1669 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
