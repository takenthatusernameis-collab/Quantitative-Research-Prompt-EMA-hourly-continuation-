# EMA Hourly Continuation — ARPA/USDT P8_55

**Symbol:** ARPA/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 805 |
| net_profit_factor | 0.7304 |
| net_win_rate | 0.4795 |
| gross_profit_factor | 0.9699 |
| gross_win_rate | 0.4807 |
| sharpe_ratio | -3.4534 |
| sortino_ratio | -1.3960 |
| max_drawdown | 0.8213 |
| cagr | -0.4720 |
| net_avg_win | 56.1844 |
| net_avg_loss | -70.8597 |
| avg_hold_time_bars | 12.2398 |
| exposure | 0.4459 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
