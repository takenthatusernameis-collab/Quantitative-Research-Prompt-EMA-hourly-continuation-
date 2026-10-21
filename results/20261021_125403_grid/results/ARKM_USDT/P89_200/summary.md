# EMA Hourly Continuation — ARKM/USDT P89_200

**Symbol:** ARKM/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 276 |
| net_profit_factor | 0.6696 |
| net_win_rate | 0.4529 |
| gross_profit_factor | 0.8074 |
| gross_win_rate | 0.4529 |
| sharpe_ratio | -1.9823 |
| sortino_ratio | -0.4670 |
| max_drawdown | 0.4281 |
| cagr | -0.1934 |
| net_avg_win | 67.6441 |
| net_avg_loss | -83.6222 |
| avg_hold_time_bars | 15.4058 |
| exposure | 0.1933 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
