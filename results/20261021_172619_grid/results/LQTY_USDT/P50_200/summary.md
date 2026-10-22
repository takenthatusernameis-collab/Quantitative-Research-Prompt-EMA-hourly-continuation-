# EMA Hourly Continuation — LQTY/USDT P50_200

**Symbol:** LQTY/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 0.7317 |
| net_win_rate | 0.4756 |
| gross_profit_factor | 0.8938 |
| gross_win_rate | 0.4756 |
| sharpe_ratio | -1.6475 |
| sortino_ratio | -0.4099 |
| max_drawdown | 0.3976 |
| cagr | -0.1720 |
| net_avg_win | 70.7632 |
| net_avg_loss | -87.7031 |
| avg_hold_time_bars | 27.8762 |
| exposure | 0.3873 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
