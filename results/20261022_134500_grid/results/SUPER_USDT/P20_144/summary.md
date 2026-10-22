# EMA Hourly Continuation — SUPER/USDT P20_144

**Symbol:** SUPER/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 540 |
| net_profit_factor | 0.7078 |
| net_win_rate | 0.4981 |
| gross_profit_factor | 1.0168 |
| gross_win_rate | 0.5093 |
| sharpe_ratio | -2.4237 |
| sortino_ratio | -0.7963 |
| max_drawdown | 0.6497 |
| cagr | -0.3146 |
| net_avg_win | 55.1621 |
| net_avg_loss | -77.3644 |
| avg_hold_time_bars | 21.7556 |
| exposure | 0.5340 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
