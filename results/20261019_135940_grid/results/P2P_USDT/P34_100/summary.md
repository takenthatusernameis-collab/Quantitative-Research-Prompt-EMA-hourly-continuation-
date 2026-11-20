# EMA Hourly Continuation — P2P/USDT P34_100

**Symbol:** P2P/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 585 |
| net_profit_factor | 0.5215 |
| net_win_rate | 0.4068 |
| gross_profit_factor | 0.6952 |
| gross_win_rate | 0.4085 |
| sharpe_ratio | -4.7366 |
| sortino_ratio | -1.6090 |
| max_drawdown | 0.8523 |
| cagr | -0.5330 |
| net_avg_win | 39.0306 |
| net_avg_loss | -51.3308 |
| avg_hold_time_bars | 10.6752 |
| exposure | 0.2839 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
