# EMA Hourly Continuation — CPOOL/USDT P26_144

**Symbol:** CPOOL/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 647 |
| net_profit_factor | 0.6972 |
| net_win_rate | 0.4745 |
| gross_profit_factor | 0.9121 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -3.1114 |
| sortino_ratio | -1.1118 |
| max_drawdown | 0.7683 |
| cagr | -0.4120 |
| net_avg_win | 55.2436 |
| net_avg_loss | -71.5440 |
| avg_hold_time_bars | 12.4621 |
| exposure | 0.3665 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
