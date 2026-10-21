# EMA Hourly Continuation — DEXE/USDT P55_100

**Symbol:** DEXE/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 301 |
| net_profit_factor | 0.7753 |
| net_win_rate | 0.5150 |
| gross_profit_factor | 1.0269 |
| gross_win_rate | 0.5150 |
| sharpe_ratio | -1.1926 |
| sortino_ratio | -0.2971 |
| max_drawdown | 0.3873 |
| cagr | -0.1279 |
| net_avg_win | 64.7398 |
| net_avg_loss | -88.6537 |
| avg_hold_time_bars | 21.6678 |
| exposure | 0.2965 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
