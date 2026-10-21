# EMA Hourly Continuation — AERO/USDT P21_34

**Symbol:** AERO/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 265 |
| net_profit_factor | 0.7337 |
| net_win_rate | 0.4981 |
| gross_profit_factor | 0.9905 |
| gross_win_rate | 0.4981 |
| sharpe_ratio | -1.5810 |
| sortino_ratio | -0.3690 |
| max_drawdown | 0.3631 |
| cagr | -0.1557 |
| net_avg_win | 72.2557 |
| net_avg_loss | -97.7415 |
| avg_hold_time_bars | 4.6226 |
| exposure | 0.0557 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
