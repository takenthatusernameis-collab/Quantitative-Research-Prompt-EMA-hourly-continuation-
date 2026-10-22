# EMA Hourly Continuation — EGLD/USDT P8_200

**Symbol:** EGLD/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.6926 |
| net_win_rate | 0.4866 |
| gross_profit_factor | 1.0010 |
| gross_win_rate | 0.4988 |
| sharpe_ratio | -2.3336 |
| sortino_ratio | -0.6625 |
| max_drawdown | 0.5738 |
| cagr | -0.2718 |
| net_avg_win | 62.1538 |
| net_avg_loss | -85.0429 |
| avg_hold_time_bars | 42.0049 |
| exposure | 0.7809 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
