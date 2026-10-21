# EMA Hourly Continuation — JASMY/USDT P50_100

**Symbol:** JASMY/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.7254 |
| net_win_rate | 0.4866 |
| gross_profit_factor | 0.9263 |
| gross_win_rate | 0.4866 |
| sharpe_ratio | -1.7394 |
| sortino_ratio | -0.4566 |
| max_drawdown | 0.4282 |
| cagr | -0.1890 |
| net_avg_win | 65.8811 |
| net_avg_loss | -86.0961 |
| avg_hold_time_bars | 9.9763 |
| exposure | 0.1528 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
