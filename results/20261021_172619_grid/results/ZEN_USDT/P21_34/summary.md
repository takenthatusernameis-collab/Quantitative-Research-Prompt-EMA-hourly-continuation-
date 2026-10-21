# EMA Hourly Continuation — ZEN/USDT P21_34

**Symbol:** ZEN/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 0.6800 |
| net_win_rate | 0.4958 |
| gross_profit_factor | 0.9824 |
| gross_win_rate | 0.4958 |
| sharpe_ratio | -2.2508 |
| sortino_ratio | -0.6089 |
| max_drawdown | 0.5067 |
| cagr | -0.2429 |
| net_avg_win | 60.7177 |
| net_avg_loss | -87.7905 |
| avg_hold_time_bars | 4.3070 |
| exposure | 0.0695 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
