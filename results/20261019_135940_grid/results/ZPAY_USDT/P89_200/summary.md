# EMA Hourly Continuation — ZPAY/USDT P89_200

**Symbol:** ZPAY/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.5097 |
| net_win_rate | 0.3890 |
| gross_profit_factor | 0.6530 |
| gross_win_rate | 0.3936 |
| sharpe_ratio | -4.1815 |
| sortino_ratio | -1.2221 |
| max_drawdown | 0.7618 |
| cagr | -0.4334 |
| net_avg_win | 46.5530 |
| net_avg_loss | -58.1576 |
| avg_hold_time_bars | 16.6453 |
| exposure | 0.3292 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
