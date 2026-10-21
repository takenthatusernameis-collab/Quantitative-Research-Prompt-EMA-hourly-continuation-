# EMA Hourly Continuation — IOTA/USDT P26_200

**Symbol:** IOTA/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 283 |
| net_profit_factor | 0.8757 |
| net_win_rate | 0.5159 |
| gross_profit_factor | 1.0585 |
| gross_win_rate | 0.5159 |
| sharpe_ratio | -0.6434 |
| sortino_ratio | -0.1555 |
| max_drawdown | 0.2429 |
| cagr | -0.0714 |
| net_avg_win | 81.8847 |
| net_avg_loss | -99.6540 |
| avg_hold_time_bars | 46.5230 |
| exposure | 0.5985 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
