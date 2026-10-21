# EMA Hourly Continuation — BIGTIME/USDT P8_12

**Symbol:** BIGTIME/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 378 |
| net_profit_factor | 0.5463 |
| net_win_rate | 0.4392 |
| gross_profit_factor | 0.7980 |
| gross_win_rate | 0.4418 |
| sharpe_ratio | -3.8192 |
| sortino_ratio | -1.0584 |
| max_drawdown | 0.7072 |
| cagr | -0.3851 |
| net_avg_win | 51.2755 |
| net_avg_loss | -73.4875 |
| avg_hold_time_bars | 5.8280 |
| exposure | 0.0997 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
