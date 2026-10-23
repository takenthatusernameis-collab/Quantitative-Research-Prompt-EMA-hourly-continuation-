# EMA Hourly Continuation — DEXE/USDT P20_144

**Symbol:** DEXE/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 394 |
| net_profit_factor | 0.7340 |
| net_win_rate | 0.5127 |
| gross_profit_factor | 1.0395 |
| gross_win_rate | 0.5152 |
| sharpe_ratio | -1.7014 |
| sortino_ratio | -0.4741 |
| max_drawdown | 0.5175 |
| cagr | -0.2050 |
| net_avg_win | 59.8235 |
| net_avg_loss | -85.7513 |
| avg_hold_time_bars | 36.7208 |
| exposure | 0.6576 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
