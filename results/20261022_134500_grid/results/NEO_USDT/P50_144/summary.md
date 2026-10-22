# EMA Hourly Continuation — NEO/USDT P50_144

**Symbol:** NEO/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 536 |
| net_profit_factor | 0.5361 |
| net_win_rate | 0.4608 |
| gross_profit_factor | 0.9191 |
| gross_win_rate | 0.4795 |
| sharpe_ratio | -4.4934 |
| sortino_ratio | -1.4698 |
| max_drawdown | 0.8321 |
| cagr | -0.5029 |
| net_avg_win | 38.7003 |
| net_avg_loss | -61.6957 |
| avg_hold_time_bars | 11.2854 |
| exposure | 0.2750 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
