# EMA Hourly Continuation — ONDO/USDT P20_34

**Symbol:** ONDO/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1120 |
| net_profit_factor | 0.4221 |
| net_win_rate | 0.4232 |
| gross_profit_factor | 0.8128 |
| gross_win_rate | 0.4393 |
| sharpe_ratio | -9.7654 |
| sortino_ratio | -4.6146 |
| max_drawdown | 0.9971 |
| cagr | -0.9025 |
| net_avg_win | 15.3672 |
| net_avg_loss | -26.7108 |
| avg_hold_time_bars | 2.5732 |
| exposure | 0.1310 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
