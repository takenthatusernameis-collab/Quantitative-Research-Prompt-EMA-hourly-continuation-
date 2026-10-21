# EMA Hourly Continuation — DBR/USDT P21_144

**Symbol:** DBR/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 290 |
| net_profit_factor | 0.6639 |
| net_win_rate | 0.4690 |
| gross_profit_factor | 0.8525 |
| gross_win_rate | 0.4690 |
| sharpe_ratio | -2.2909 |
| sortino_ratio | -0.6203 |
| max_drawdown | 0.4707 |
| cagr | -0.2485 |
| net_avg_win | 63.3839 |
| net_avg_loss | -84.3107 |
| avg_hold_time_bars | 32.1138 |
| exposure | 0.5296 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
