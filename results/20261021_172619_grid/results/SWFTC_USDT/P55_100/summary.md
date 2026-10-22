# EMA Hourly Continuation — SWFTC/USDT P55_100

**Symbol:** SWFTC/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 256 |
| net_profit_factor | 0.7892 |
| net_win_rate | 0.5078 |
| gross_profit_factor | 1.0307 |
| gross_win_rate | 0.5078 |
| sharpe_ratio | -1.1913 |
| sortino_ratio | -0.2737 |
| max_drawdown | 0.2826 |
| cagr | -0.1186 |
| net_avg_win | 78.2547 |
| net_avg_loss | -102.3007 |
| avg_hold_time_bars | 8.2109 |
| exposure | 0.0955 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
