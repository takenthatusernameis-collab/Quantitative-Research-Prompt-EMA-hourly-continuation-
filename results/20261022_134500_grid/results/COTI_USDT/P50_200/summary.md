# EMA Hourly Continuation — COTI/USDT P50_200

**Symbol:** COTI/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.8171 |
| net_win_rate | 0.5335 |
| gross_profit_factor | 1.1890 |
| gross_win_rate | 0.5490 |
| sharpe_ratio | -1.1480 |
| sortino_ratio | -0.3202 |
| max_drawdown | 0.3751 |
| cagr | -0.1441 |
| net_avg_win | 69.8251 |
| net_avg_loss | -97.7277 |
| avg_hold_time_bars | 22.8763 |
| exposure | 0.4035 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
