# EMA Hourly Continuation — RAY/USDT P8_34

**Symbol:** RAY/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1349 |
| net_profit_factor | 0.6420 |
| net_win_rate | 0.4744 |
| gross_profit_factor | 1.0327 |
| gross_win_rate | 0.4885 |
| sharpe_ratio | -6.3563 |
| sortino_ratio | -3.2786 |
| max_drawdown | 0.9814 |
| cagr | -0.7953 |
| net_avg_win | 27.5005 |
| net_avg_loss | -38.6660 |
| avg_hold_time_bars | 5.6227 |
| exposure | 0.3448 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
