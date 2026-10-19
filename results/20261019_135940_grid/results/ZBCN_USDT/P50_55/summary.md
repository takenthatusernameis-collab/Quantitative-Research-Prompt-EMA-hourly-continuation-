# EMA Hourly Continuation — ZBCN/USDT P50_55

**Symbol:** ZBCN/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 842 |
| net_profit_factor | 0.2081 |
| net_win_rate | 0.3361 |
| gross_profit_factor | 0.6085 |
| gross_win_rate | 0.3634 |
| sharpe_ratio | -12.5187 |
| sortino_ratio | -5.2900 |
| max_drawdown | 0.9992 |
| cagr | -0.9457 |
| net_avg_win | 9.2761 |
| net_avg_loss | -22.5717 |
| avg_hold_time_bars | 1.7007 |
| exposure | 0.0663 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
