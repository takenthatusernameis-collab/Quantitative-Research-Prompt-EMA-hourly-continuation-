# EMA Hourly Continuation — ORBS/USDT P21_50

**Symbol:** ORBS/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1009 |
| net_profit_factor | 0.4030 |
| net_win_rate | 0.3954 |
| gross_profit_factor | 0.8759 |
| gross_win_rate | 0.4272 |
| sharpe_ratio | -10.0959 |
| sortino_ratio | -4.5279 |
| max_drawdown | 0.9969 |
| cagr | -0.8989 |
| net_avg_win | 16.8671 |
| net_avg_loss | -27.3742 |
| avg_hold_time_bars | 5.9049 |
| exposure | 0.2708 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
