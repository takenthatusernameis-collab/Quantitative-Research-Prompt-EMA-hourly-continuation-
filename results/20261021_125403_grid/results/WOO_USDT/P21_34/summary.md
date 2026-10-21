# EMA Hourly Continuation — WOO/USDT P21_34

**Symbol:** WOO/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 398 |
| net_profit_factor | 0.6841 |
| net_win_rate | 0.4749 |
| gross_profit_factor | 0.9506 |
| gross_win_rate | 0.4749 |
| sharpe_ratio | -2.7446 |
| sortino_ratio | -0.7833 |
| max_drawdown | 0.6496 |
| cagr | -0.3024 |
| net_avg_win | 68.1940 |
| net_avg_loss | -90.1476 |
| avg_hold_time_bars | 4.9698 |
| exposure | 0.0899 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
