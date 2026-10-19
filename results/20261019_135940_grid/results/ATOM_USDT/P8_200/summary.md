# EMA Hourly Continuation — ATOM/USDT P8_200

**Symbol:** ATOM/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 0.6650 |
| net_win_rate | 0.4864 |
| gross_profit_factor | 0.9788 |
| gross_win_rate | 0.4942 |
| sharpe_ratio | -1.9712 |
| sortino_ratio | -0.4391 |
| max_drawdown | 0.4346 |
| cagr | -0.1929 |
| net_avg_win | 66.0988 |
| net_avg_loss | -94.1260 |
| avg_hold_time_bars | 73.2607 |
| exposure | 0.8558 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
