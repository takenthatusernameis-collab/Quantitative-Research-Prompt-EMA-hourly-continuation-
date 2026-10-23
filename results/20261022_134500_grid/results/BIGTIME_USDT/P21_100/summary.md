# EMA Hourly Continuation — BIGTIME/USDT P21_100

**Symbol:** BIGTIME/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 608 |
| net_profit_factor | 0.7063 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0306 |
| gross_win_rate | 0.5066 |
| sharpe_ratio | -2.6988 |
| sortino_ratio | -0.9378 |
| max_drawdown | 0.7048 |
| cagr | -0.3597 |
| net_avg_win | 53.4053 |
| net_avg_loss | -75.6143 |
| avg_hold_time_bars | 16.7155 |
| exposure | 0.4599 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
