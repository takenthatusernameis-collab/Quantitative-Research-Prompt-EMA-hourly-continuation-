# EMA Hourly Continuation — AERO/USDT P12_144

**Symbol:** AERO/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.9385 |
| net_win_rate | 0.5184 |
| gross_profit_factor | 1.0709 |
| gross_win_rate | 0.5184 |
| sharpe_ratio | -0.3909 |
| sortino_ratio | -0.1095 |
| max_drawdown | 0.3075 |
| cagr | -0.0542 |
| net_avg_win | 101.1173 |
| net_avg_loss | -115.9904 |
| avg_hold_time_bars | 36.6921 |
| exposure | 0.6338 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
