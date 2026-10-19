# EMA Hourly Continuation — FLOKI/USDT P12_55

**Symbol:** FLOKI/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1073 |
| net_profit_factor | 0.5583 |
| net_win_rate | 0.4595 |
| gross_profit_factor | 0.8436 |
| gross_win_rate | 0.4641 |
| sharpe_ratio | -6.5569 |
| sortino_ratio | -3.0032 |
| max_drawdown | 0.9758 |
| cagr | -0.7716 |
| net_avg_win | 25.0116 |
| net_avg_loss | -38.0783 |
| avg_hold_time_bars | 7.8425 |
| exposure | 0.3825 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
