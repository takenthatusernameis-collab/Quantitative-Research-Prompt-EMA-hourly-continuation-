# EMA Hourly Continuation — RSR/USDT P21_144

**Symbol:** RSR/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 480 |
| net_profit_factor | 0.7832 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0083 |
| gross_win_rate | 0.5021 |
| sharpe_ratio | -1.7523 |
| sortino_ratio | -0.5468 |
| max_drawdown | 0.5180 |
| cagr | -0.2257 |
| net_avg_win | 71.3300 |
| net_avg_loss | -91.0802 |
| avg_hold_time_bars | 24.1042 |
| exposure | 0.5259 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
