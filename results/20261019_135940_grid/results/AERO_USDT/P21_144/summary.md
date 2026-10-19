# EMA Hourly Continuation — AERO/USDT P21_144

**Symbol:** AERO/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.8796 |
| net_win_rate | 0.5349 |
| gross_profit_factor | 1.1624 |
| gross_win_rate | 0.5373 |
| sharpe_ratio | -0.8164 |
| sortino_ratio | -0.2380 |
| max_drawdown | 0.3021 |
| cagr | -0.1089 |
| net_avg_win | 82.7571 |
| net_avg_loss | -108.2187 |
| avg_hold_time_bars | 28.2361 |
| exposure | 0.5326 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
