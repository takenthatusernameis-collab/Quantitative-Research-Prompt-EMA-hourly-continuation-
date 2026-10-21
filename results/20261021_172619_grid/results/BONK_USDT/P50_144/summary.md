# EMA Hourly Continuation — BONK/USDT P50_144

**Symbol:** BONK/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 311 |
| net_profit_factor | 0.8132 |
| net_win_rate | 0.4984 |
| gross_profit_factor | 0.9711 |
| gross_win_rate | 0.4984 |
| sharpe_ratio | -1.0724 |
| sortino_ratio | -0.2702 |
| max_drawdown | 0.3315 |
| cagr | -0.1185 |
| net_avg_win | 76.2458 |
| net_avg_loss | -93.1579 |
| avg_hold_time_bars | 19.7106 |
| exposure | 0.2786 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
