# EMA Hourly Continuation — CPOOL/USDT P26_200

**Symbol:** CPOOL/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 536 |
| net_profit_factor | 0.5969 |
| net_win_rate | 0.4328 |
| gross_profit_factor | 0.7660 |
| gross_win_rate | 0.4328 |
| sharpe_ratio | -4.0140 |
| sortino_ratio | -1.3010 |
| max_drawdown | 0.8127 |
| cagr | -0.4639 |
| net_avg_win | 50.4898 |
| net_avg_loss | -64.5544 |
| avg_hold_time_bars | 18.6996 |
| exposure | 0.4556 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
