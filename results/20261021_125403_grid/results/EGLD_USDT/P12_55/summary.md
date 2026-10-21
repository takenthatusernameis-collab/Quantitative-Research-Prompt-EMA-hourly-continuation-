# EMA Hourly Continuation — EGLD/USDT P12_55

**Symbol:** EGLD/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 642 |
| net_profit_factor | 0.7567 |
| net_win_rate | 0.4922 |
| gross_profit_factor | 0.9968 |
| gross_win_rate | 0.4922 |
| sharpe_ratio | -2.4790 |
| sortino_ratio | -0.8991 |
| max_drawdown | 0.6719 |
| cagr | -0.3385 |
| net_avg_win | 63.5421 |
| net_avg_loss | -81.4022 |
| avg_hold_time_bars | 12.3801 |
| exposure | 0.3613 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
