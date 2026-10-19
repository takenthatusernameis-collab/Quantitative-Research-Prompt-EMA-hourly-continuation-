# EMA Hourly Continuation — AVAX/USDT P20_55

**Symbol:** AVAX/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 924 |
| net_profit_factor | 0.5301 |
| net_win_rate | 0.4416 |
| gross_profit_factor | 0.9416 |
| gross_win_rate | 0.4567 |
| sharpe_ratio | -7.6341 |
| sortino_ratio | -3.2564 |
| max_drawdown | 0.9835 |
| cagr | -0.8025 |
| net_avg_win | 27.1758 |
| net_avg_loss | -40.5377 |
| avg_hold_time_bars | 5.0639 |
| exposure | 0.2127 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
