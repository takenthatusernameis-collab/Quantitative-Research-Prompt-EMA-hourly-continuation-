# EMA Hourly Continuation — ENA/USDT P50_55

**Symbol:** ENA/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 85 |
| net_profit_factor | 0.8779 |
| net_win_rate | 0.5294 |
| gross_profit_factor | 1.1157 |
| gross_win_rate | 0.5294 |
| sharpe_ratio | -0.3525 |
| sortino_ratio | -0.0469 |
| max_drawdown | 0.1550 |
| cagr | -0.0219 |
| net_avg_win | 86.4509 |
| net_avg_loss | -110.7799 |
| avg_hold_time_bars | 5.7412 |
| exposure | 0.0222 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
