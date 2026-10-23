# EMA Hourly Continuation — CFG/USDT P21_100

**Symbol:** CFG/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 569 |
| net_profit_factor | 0.6107 |
| net_win_rate | 0.4534 |
| gross_profit_factor | 0.8670 |
| gross_win_rate | 0.4569 |
| sharpe_ratio | -3.6689 |
| sortino_ratio | -1.2386 |
| max_drawdown | 0.7727 |
| cagr | -0.4393 |
| net_avg_win | 46.5821 |
| net_avg_loss | -63.2769 |
| avg_hold_time_bars | 19.8717 |
| exposure | 0.5140 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
