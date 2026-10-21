# EMA Hourly Continuation — AUCTION/USDT P8_20

**Symbol:** AUCTION/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 750 |
| net_profit_factor | 0.5815 |
| net_win_rate | 0.4427 |
| gross_profit_factor | 0.8673 |
| gross_win_rate | 0.4440 |
| sharpe_ratio | -5.8295 |
| sortino_ratio | -2.2727 |
| max_drawdown | 0.9343 |
| cagr | -0.6566 |
| net_avg_win | 39.0296 |
| net_avg_loss | -53.3083 |
| avg_hold_time_bars | 6.2240 |
| exposure | 0.2113 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
