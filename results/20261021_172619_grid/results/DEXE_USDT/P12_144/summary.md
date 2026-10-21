# EMA Hourly Continuation — DEXE/USDT P12_144

**Symbol:** DEXE/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 327 |
| net_profit_factor | 0.9756 |
| net_win_rate | 0.5413 |
| gross_profit_factor | 1.1599 |
| gross_win_rate | 0.5413 |
| sharpe_ratio | -0.0741 |
| sortino_ratio | -0.0194 |
| max_drawdown | 0.2521 |
| cagr | -0.0148 |
| net_avg_win | 83.2659 |
| net_avg_loss | -100.7111 |
| avg_hold_time_bars | 49.3639 |
| exposure | 0.7337 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
