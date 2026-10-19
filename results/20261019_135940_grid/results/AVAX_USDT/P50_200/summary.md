# EMA Hourly Continuation — AVAX/USDT P50_200

**Symbol:** AVAX/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 359 |
| net_profit_factor | 0.5621 |
| net_win_rate | 0.4540 |
| gross_profit_factor | 0.8728 |
| gross_win_rate | 0.4652 |
| sharpe_ratio | -3.5428 |
| sortino_ratio | -0.9378 |
| max_drawdown | 0.6899 |
| cagr | -0.3685 |
| net_avg_win | 53.9164 |
| net_avg_loss | -79.7765 |
| avg_hold_time_bars | 22.8412 |
| exposure | 0.3727 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
