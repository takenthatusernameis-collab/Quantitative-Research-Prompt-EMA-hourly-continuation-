# EMA Hourly Continuation — FIL/USDT P21_144

**Symbol:** FIL/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.5876 |
| net_win_rate | 0.4547 |
| gross_profit_factor | 0.8808 |
| gross_win_rate | 0.4648 |
| sharpe_ratio | -3.7983 |
| sortino_ratio | -1.1943 |
| max_drawdown | 0.7728 |
| cagr | -0.4315 |
| net_avg_win | 47.7889 |
| net_avg_loss | -67.8186 |
| avg_hold_time_bars | 22.7787 |
| exposure | 0.5146 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
