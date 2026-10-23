# EMA Hourly Continuation — IOTX/USDT P12_100

**Symbol:** IOTX/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 714 |
| net_profit_factor | 0.5603 |
| net_win_rate | 0.4636 |
| gross_profit_factor | 0.8646 |
| gross_win_rate | 0.4720 |
| sharpe_ratio | -4.6780 |
| sortino_ratio | -1.7508 |
| max_drawdown | 0.8864 |
| cagr | -0.5710 |
| net_avg_win | 33.8965 |
| net_avg_loss | -52.2862 |
| avg_hold_time_bars | 17.1821 |
| exposure | 0.5576 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
