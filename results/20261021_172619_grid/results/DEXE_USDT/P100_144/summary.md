# EMA Hourly Continuation — DEXE/USDT P100_144

**Symbol:** DEXE/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 194 |
| net_profit_factor | 0.8176 |
| net_win_rate | 0.5309 |
| gross_profit_factor | 1.1078 |
| gross_win_rate | 0.5309 |
| sharpe_ratio | -0.7800 |
| sortino_ratio | -0.1568 |
| max_drawdown | 0.2511 |
| cagr | -0.0703 |
| net_avg_win | 72.7991 |
| net_avg_loss | -100.7836 |
| avg_hold_time_bars | 20.0464 |
| exposure | 0.1768 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
