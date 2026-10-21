# EMA Hourly Continuation — CSPR/USDT P89_144

**Symbol:** CSPR/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.6936 |
| net_win_rate | 0.4764 |
| gross_profit_factor | 0.9002 |
| gross_win_rate | 0.4764 |
| sharpe_ratio | -1.8497 |
| sortino_ratio | -0.4380 |
| max_drawdown | 0.4214 |
| cagr | -0.1824 |
| net_avg_win | 68.5850 |
| net_avg_loss | -89.9622 |
| avg_hold_time_bars | 8.9164 |
| exposure | 0.1115 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
