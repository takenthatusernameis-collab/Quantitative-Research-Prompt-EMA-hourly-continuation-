# EMA Hourly Continuation — POPCAT/USDT P12_100

**Symbol:** POPCAT/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.8699 |
| net_win_rate | 0.5013 |
| gross_profit_factor | 1.0033 |
| gross_win_rate | 0.5013 |
| sharpe_ratio | -0.9092 |
| sortino_ratio | -0.2703 |
| max_drawdown | 0.3303 |
| cagr | -0.1204 |
| net_avg_win | 87.0649 |
| net_avg_loss | -100.6253 |
| avg_hold_time_bars | 29.4420 |
| exposure | 0.5770 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
