# EMA Hourly Continuation — APT/USDT P89_200

**Symbol:** APT/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.6146 |
| net_win_rate | 0.4686 |
| gross_profit_factor | 0.9276 |
| gross_win_rate | 0.4712 |
| sharpe_ratio | -3.1214 |
| sortino_ratio | -0.8591 |
| max_drawdown | 0.6468 |
| cagr | -0.3369 |
| net_avg_win | 57.3481 |
| net_avg_loss | -82.2750 |
| avg_hold_time_bars | 10.3874 |
| exposure | 0.1804 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
