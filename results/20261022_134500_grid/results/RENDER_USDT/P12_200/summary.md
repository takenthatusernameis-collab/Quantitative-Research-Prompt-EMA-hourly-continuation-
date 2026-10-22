# EMA Hourly Continuation — RENDER/USDT P12_200

**Symbol:** RENDER/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 260 |
| net_profit_factor | 0.7256 |
| net_win_rate | 0.4885 |
| gross_profit_factor | 0.9393 |
| gross_win_rate | 0.4885 |
| sharpe_ratio | -1.6786 |
| sortino_ratio | -0.4091 |
| max_drawdown | 0.4148 |
| cagr | -0.1784 |
| net_avg_win | 72.0959 |
| net_avg_loss | -94.8750 |
| avg_hold_time_bars | 58.4769 |
| exposure | 0.8024 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
