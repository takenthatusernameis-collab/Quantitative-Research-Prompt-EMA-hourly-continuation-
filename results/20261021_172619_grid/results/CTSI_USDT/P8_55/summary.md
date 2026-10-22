# EMA Hourly Continuation — CTSI/USDT P8_55

**Symbol:** CTSI/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 757 |
| net_profit_factor | 0.7657 |
| net_win_rate | 0.4835 |
| gross_profit_factor | 0.9892 |
| gross_win_rate | 0.4835 |
| sharpe_ratio | -2.8624 |
| sortino_ratio | -1.1236 |
| max_drawdown | 0.7337 |
| cagr | -0.4036 |
| net_avg_win | 64.9173 |
| net_avg_loss | -79.3583 |
| avg_hold_time_bars | 12.9934 |
| exposure | 0.4471 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
