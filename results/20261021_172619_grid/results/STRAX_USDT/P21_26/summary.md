# EMA Hourly Continuation — STRAX/USDT P21_26

**Symbol:** STRAX/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.4384 |
| net_win_rate | 0.4133 |
| gross_profit_factor | 0.7015 |
| gross_win_rate | 0.4157 |
| sharpe_ratio | -5.2188 |
| sortino_ratio | -1.5361 |
| max_drawdown | 0.8321 |
| cagr | -0.5091 |
| net_avg_win | 37.2680 |
| net_avg_loss | -59.8868 |
| avg_hold_time_bars | 6.0333 |
| exposure | 0.1161 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
