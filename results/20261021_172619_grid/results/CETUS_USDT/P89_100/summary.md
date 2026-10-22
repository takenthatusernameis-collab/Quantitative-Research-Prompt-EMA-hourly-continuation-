# EMA Hourly Continuation — CETUS/USDT P89_100

**Symbol:** CETUS/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 138 |
| net_profit_factor | 0.7584 |
| net_win_rate | 0.5217 |
| gross_profit_factor | 1.0827 |
| gross_win_rate | 0.5217 |
| sharpe_ratio | -0.9804 |
| sortino_ratio | -0.1656 |
| max_drawdown | 0.1884 |
| cagr | -0.0731 |
| net_avg_win | 76.0051 |
| net_avg_loss | -109.3215 |
| avg_hold_time_bars | 4.4493 |
| exposure | 0.0278 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
