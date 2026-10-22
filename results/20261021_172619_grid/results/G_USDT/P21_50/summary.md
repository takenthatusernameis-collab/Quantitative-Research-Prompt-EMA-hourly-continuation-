# EMA Hourly Continuation — G/USDT P21_50

**Symbol:** G/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.5876 |
| net_win_rate | 0.4558 |
| gross_profit_factor | 0.8462 |
| gross_win_rate | 0.4558 |
| sharpe_ratio | -4.1436 |
| sortino_ratio | -1.4518 |
| max_drawdown | 0.7827 |
| cagr | -0.4862 |
| net_avg_win | 45.9611 |
| net_avg_loss | -65.5017 |
| avg_hold_time_bars | 8.8269 |
| exposure | 0.2414 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
