# EMA Hourly Continuation — BOME/USDT P8_200

**Symbol:** BOME/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.7778 |
| net_win_rate | 0.5067 |
| gross_profit_factor | 1.0127 |
| gross_win_rate | 0.5067 |
| sharpe_ratio | -1.4565 |
| sortino_ratio | -0.3997 |
| max_drawdown | 0.4107 |
| cagr | -0.1705 |
| net_avg_win | 69.4058 |
| net_avg_loss | -91.6573 |
| avg_hold_time_bars | 47.5469 |
| exposure | 0.8061 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
