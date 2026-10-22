# EMA Hourly Continuation — LISTA/USDT P8_144

**Symbol:** LISTA/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.8715 |
| net_win_rate | 0.5064 |
| gross_profit_factor | 1.0263 |
| gross_win_rate | 0.5064 |
| sharpe_ratio | -0.8762 |
| sortino_ratio | -0.2578 |
| max_drawdown | 0.3172 |
| cagr | -0.1152 |
| net_avg_win | 84.6878 |
| net_avg_loss | -99.6834 |
| avg_hold_time_bars | 36.1069 |
| exposure | 0.6939 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
