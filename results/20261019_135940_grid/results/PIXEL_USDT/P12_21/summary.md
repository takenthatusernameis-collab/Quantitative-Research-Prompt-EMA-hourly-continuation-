# EMA Hourly Continuation — PIXEL/USDT P12_21

**Symbol:** PIXEL/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1453 |
| net_profit_factor | 0.4057 |
| net_win_rate | 0.4336 |
| gross_profit_factor | 0.8708 |
| gross_win_rate | 0.4584 |
| sharpe_ratio | -10.6601 |
| sortino_ratio | -5.7140 |
| max_drawdown | 0.9993 |
| cagr | -0.9434 |
| net_avg_win | 10.8271 |
| net_avg_loss | -20.4300 |
| avg_hold_time_bars | 2.7832 |
| exposure | 0.1830 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
