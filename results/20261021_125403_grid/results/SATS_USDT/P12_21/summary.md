# EMA Hourly Continuation — SATS/USDT P12_21

**Symbol:** SATS/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.7791 |
| net_win_rate | 0.5166 |
| gross_profit_factor | 1.0767 |
| gross_win_rate | 0.5166 |
| sharpe_ratio | -1.5919 |
| sortino_ratio | -0.4510 |
| max_drawdown | 0.4349 |
| cagr | -0.1885 |
| net_avg_win | 71.5178 |
| net_avg_loss | -98.1081 |
| avg_hold_time_bars | 5.0077 |
| exposure | 0.0886 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
