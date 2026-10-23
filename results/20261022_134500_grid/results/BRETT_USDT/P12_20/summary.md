# EMA Hourly Continuation — BRETT/USDT P12_20

**Symbol:** BRETT/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1389 |
| net_profit_factor | 0.4512 |
| net_win_rate | 0.4276 |
| gross_profit_factor | 0.8240 |
| gross_win_rate | 0.4456 |
| sharpe_ratio | -10.6349 |
| sortino_ratio | -5.7446 |
| max_drawdown | 0.9989 |
| cagr | -0.9444 |
| net_avg_win | 13.8283 |
| net_avg_loss | -22.8975 |
| avg_hold_time_bars | 2.3715 |
| exposure | 0.1585 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
