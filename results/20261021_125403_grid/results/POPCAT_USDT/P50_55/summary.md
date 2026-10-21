# EMA Hourly Continuation — POPCAT/USDT P50_55

**Symbol:** POPCAT/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 136 |
| net_profit_factor | 0.5675 |
| net_win_rate | 0.4412 |
| gross_profit_factor | 0.7827 |
| gross_win_rate | 0.4412 |
| sharpe_ratio | -2.2049 |
| sortino_ratio | -0.3944 |
| max_drawdown | 0.3506 |
| cagr | -0.1655 |
| net_avg_win | 70.7392 |
| net_avg_loss | -98.4163 |
| avg_hold_time_bars | 4.9118 |
| exposure | 0.0353 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
