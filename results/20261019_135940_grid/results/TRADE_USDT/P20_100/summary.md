# EMA Hourly Continuation — TRADE/USDT P20_100

**Symbol:** TRADE/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 533 |
| net_profit_factor | 0.5981 |
| net_win_rate | 0.4522 |
| gross_profit_factor | 0.8500 |
| gross_win_rate | 0.4522 |
| sharpe_ratio | -3.9472 |
| sortino_ratio | -1.2642 |
| max_drawdown | 0.7989 |
| cagr | -0.4658 |
| net_avg_win | 48.9582 |
| net_avg_loss | -67.5625 |
| avg_hold_time_bars | 16.8255 |
| exposure | 0.4076 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
