# EMA Hourly Continuation — METIS/USDT P26_200

**Symbol:** METIS/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 296 |
| net_profit_factor | 0.6985 |
| net_win_rate | 0.4527 |
| gross_profit_factor | 0.8288 |
| gross_win_rate | 0.4527 |
| sharpe_ratio | -1.9622 |
| sortino_ratio | -0.4780 |
| max_drawdown | 0.4304 |
| cagr | -0.1978 |
| net_avg_win | 73.5024 |
| net_avg_loss | -87.0402 |
| avg_hold_time_bars | 43.3986 |
| exposure | 0.5839 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
