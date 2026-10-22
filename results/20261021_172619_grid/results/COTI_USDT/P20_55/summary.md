# EMA Hourly Continuation — COTI/USDT P20_55

**Symbol:** COTI/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.8012 |
| net_win_rate | 0.4952 |
| gross_profit_factor | 1.0080 |
| gross_win_rate | 0.4952 |
| sharpe_ratio | -1.8266 |
| sortino_ratio | -0.5958 |
| max_drawdown | 0.5665 |
| cagr | -0.2399 |
| net_avg_win | 78.0902 |
| net_avg_loss | -95.6025 |
| avg_hold_time_bars | 8.3237 |
| exposure | 0.1964 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
