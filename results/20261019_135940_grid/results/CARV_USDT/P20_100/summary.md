# EMA Hourly Continuation — CARV/USDT P20_100

**Symbol:** CARV/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 506 |
| net_profit_factor | 0.6206 |
| net_win_rate | 0.4723 |
| gross_profit_factor | 0.9650 |
| gross_win_rate | 0.4862 |
| sharpe_ratio | -3.9251 |
| sortino_ratio | -1.3710 |
| max_drawdown | 0.7511 |
| cagr | -0.4840 |
| net_avg_win | 50.5619 |
| net_avg_loss | -72.9279 |
| avg_hold_time_bars | 15.2470 |
| exposure | 0.4342 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
