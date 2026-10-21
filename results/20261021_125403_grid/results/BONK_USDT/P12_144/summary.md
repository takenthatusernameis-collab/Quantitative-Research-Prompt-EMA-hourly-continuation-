# EMA Hourly Continuation — BONK/USDT P12_144

**Symbol:** BONK/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.9137 |
| net_win_rate | 0.5136 |
| gross_profit_factor | 1.0518 |
| gross_win_rate | 0.5166 |
| sharpe_ratio | -0.4752 |
| sortino_ratio | -0.1241 |
| max_drawdown | 0.2559 |
| cagr | -0.0595 |
| net_avg_win | 88.8996 |
| net_avg_loss | -102.7372 |
| avg_hold_time_bars | 45.2477 |
| exposure | 0.6808 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
