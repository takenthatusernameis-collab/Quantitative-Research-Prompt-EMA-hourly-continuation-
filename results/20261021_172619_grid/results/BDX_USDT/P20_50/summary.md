# EMA Hourly Continuation — BDX/USDT P20_50

**Symbol:** BDX/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 319 |
| net_profit_factor | 0.4208 |
| net_win_rate | 0.4013 |
| gross_profit_factor | 0.6978 |
| gross_win_rate | 0.4013 |
| sharpe_ratio | -4.9522 |
| sortino_ratio | -1.2678 |
| max_drawdown | 0.7853 |
| cagr | -0.4488 |
| net_avg_win | 44.0315 |
| net_avg_loss | -70.1319 |
| avg_hold_time_bars | 8.9561 |
| exposure | 0.1299 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
