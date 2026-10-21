# EMA Hourly Continuation — CHR/USDT P89_100

**Symbol:** CHR/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 161 |
| net_profit_factor | 0.7238 |
| net_win_rate | 0.5031 |
| gross_profit_factor | 1.0051 |
| gross_win_rate | 0.5031 |
| sharpe_ratio | -1.2482 |
| sortino_ratio | -0.2272 |
| max_drawdown | 0.2726 |
| cagr | -0.0987 |
| net_avg_win | 74.5766 |
| net_avg_loss | -104.3276 |
| avg_hold_time_bars | 4.9503 |
| exposure | 0.0361 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
