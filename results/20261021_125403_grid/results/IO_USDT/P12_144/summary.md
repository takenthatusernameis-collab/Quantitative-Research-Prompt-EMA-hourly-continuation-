# EMA Hourly Continuation — IO/USDT P12_144

**Symbol:** IO/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 327 |
| net_profit_factor | 0.8089 |
| net_win_rate | 0.4832 |
| gross_profit_factor | 0.9334 |
| gross_win_rate | 0.4832 |
| sharpe_ratio | -1.2372 |
| sortino_ratio | -0.3292 |
| max_drawdown | 0.3518 |
| cagr | -0.1420 |
| net_avg_win | 81.1660 |
| net_avg_loss | -93.8149 |
| avg_hold_time_bars | 42.7125 |
| exposure | 0.6762 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
