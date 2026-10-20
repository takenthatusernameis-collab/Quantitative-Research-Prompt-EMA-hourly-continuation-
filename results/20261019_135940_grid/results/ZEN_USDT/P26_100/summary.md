# EMA Hourly Continuation — ZEN/USDT P26_100

**Symbol:** ZEN/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 690 |
| net_profit_factor | 0.5536 |
| net_win_rate | 0.4507 |
| gross_profit_factor | 0.8527 |
| gross_win_rate | 0.4638 |
| sharpe_ratio | -4.7423 |
| sortino_ratio | -1.7549 |
| max_drawdown | 0.8831 |
| cagr | -0.5677 |
| net_avg_win | 35.0248 |
| net_avg_loss | -51.9144 |
| avg_hold_time_bars | 11.2174 |
| exposure | 0.3518 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
