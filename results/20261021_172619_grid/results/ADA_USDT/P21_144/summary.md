# EMA Hourly Continuation — ADA/USDT P21_144

**Symbol:** ADA/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.8554 |
| net_win_rate | 0.5173 |
| gross_profit_factor | 1.0596 |
| gross_win_rate | 0.5173 |
| sharpe_ratio | -0.8762 |
| sortino_ratio | -0.2340 |
| max_drawdown | 0.2927 |
| cagr | -0.1041 |
| net_avg_win | 79.7238 |
| net_avg_loss | -99.9005 |
| avg_hold_time_bars | 33.0491 |
| exposure | 0.5198 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
