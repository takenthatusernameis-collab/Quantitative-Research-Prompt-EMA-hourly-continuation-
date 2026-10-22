# EMA Hourly Continuation — NEO/USDT P21_55

**Symbol:** NEO/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 960 |
| net_profit_factor | 0.3617 |
| net_win_rate | 0.4240 |
| gross_profit_factor | 0.7351 |
| gross_win_rate | 0.4354 |
| sharpe_ratio | -8.6588 |
| sortino_ratio | -3.7760 |
| max_drawdown | 0.9911 |
| cagr | -0.8474 |
| net_avg_win | 13.8006 |
| net_avg_loss | -28.0792 |
| avg_hold_time_bars | 5.5969 |
| exposure | 0.2442 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
