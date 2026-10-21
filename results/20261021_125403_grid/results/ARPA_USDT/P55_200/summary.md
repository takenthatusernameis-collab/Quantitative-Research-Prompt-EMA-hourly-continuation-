# EMA Hourly Continuation — ARPA/USDT P55_200

**Symbol:** ARPA/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 370 |
| net_profit_factor | 0.6400 |
| net_win_rate | 0.4622 |
| gross_profit_factor | 0.8335 |
| gross_win_rate | 0.4622 |
| sharpe_ratio | -2.5976 |
| sortino_ratio | -0.7089 |
| max_drawdown | 0.5814 |
| cagr | -0.2792 |
| net_avg_win | 58.4422 |
| net_avg_loss | -78.4699 |
| avg_hold_time_bars | 21.0297 |
| exposure | 0.3521 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
