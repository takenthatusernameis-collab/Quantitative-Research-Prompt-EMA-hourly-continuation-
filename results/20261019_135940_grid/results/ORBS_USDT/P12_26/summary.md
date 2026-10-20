# EMA Hourly Continuation — ORBS/USDT P12_26

**Symbol:** ORBS/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1351 |
| net_profit_factor | 0.2928 |
| net_win_rate | 0.3649 |
| gross_profit_factor | 0.8065 |
| gross_win_rate | 0.4064 |
| sharpe_ratio | -13.9619 |
| sortino_ratio | -7.3394 |
| max_drawdown | 0.9999 |
| cagr | -0.9774 |
| net_avg_win | 8.3992 |
| net_avg_loss | -16.4803 |
| avg_hold_time_bars | 4.4241 |
| exposure | 0.2717 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
