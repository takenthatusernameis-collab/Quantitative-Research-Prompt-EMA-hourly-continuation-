# EMA Hourly Continuation — VELO/USDT P21_144

**Symbol:** VELO/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 566 |
| net_profit_factor | 0.8260 |
| net_win_rate | 0.5177 |
| gross_profit_factor | 1.0743 |
| gross_win_rate | 0.5177 |
| sharpe_ratio | -1.4923 |
| sortino_ratio | -0.5046 |
| max_drawdown | 0.5726 |
| cagr | -0.2135 |
| net_avg_win | 73.3896 |
| net_avg_loss | -95.3562 |
| avg_hold_time_bars | 20.3940 |
| exposure | 0.5247 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
