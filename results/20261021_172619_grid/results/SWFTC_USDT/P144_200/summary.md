# EMA Hourly Continuation — SWFTC/USDT P144_200

**Symbol:** SWFTC/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 167 |
| net_profit_factor | 0.7601 |
| net_win_rate | 0.4970 |
| gross_profit_factor | 0.9911 |
| gross_win_rate | 0.4970 |
| sharpe_ratio | -1.1229 |
| sortino_ratio | -0.2079 |
| max_drawdown | 0.2435 |
| cagr | -0.0909 |
| net_avg_win | 81.2206 |
| net_avg_loss | -105.5898 |
| avg_hold_time_bars | 9.5090 |
| exposure | 0.0722 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
