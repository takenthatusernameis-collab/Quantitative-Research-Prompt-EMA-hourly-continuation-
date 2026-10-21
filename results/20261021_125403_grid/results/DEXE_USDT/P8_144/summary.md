# EMA Hourly Continuation — DEXE/USDT P8_144

**Symbol:** DEXE/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.9214 |
| net_win_rate | 0.5277 |
| gross_profit_factor | 1.0929 |
| gross_win_rate | 0.5277 |
| sharpe_ratio | -0.3801 |
| sortino_ratio | -0.1013 |
| max_drawdown | 0.3368 |
| cagr | -0.0501 |
| net_avg_win | 78.4483 |
| net_avg_loss | -95.1289 |
| avg_hold_time_bars | 50.2799 |
| exposure | 0.7839 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
