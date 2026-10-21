# EMA Hourly Continuation — FLOW/USDT P26_200

**Symbol:** FLOW/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 311 |
| net_profit_factor | 0.7123 |
| net_win_rate | 0.4630 |
| gross_profit_factor | 0.8583 |
| gross_win_rate | 0.4630 |
| sharpe_ratio | -1.8802 |
| sortino_ratio | -0.4702 |
| max_drawdown | 0.4396 |
| cagr | -0.1954 |
| net_avg_win | 72.3241 |
| net_avg_loss | -87.5569 |
| avg_hold_time_bars | 40.4630 |
| exposure | 0.5720 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
