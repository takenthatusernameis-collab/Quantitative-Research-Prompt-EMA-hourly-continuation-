# EMA Hourly Continuation — ZPAY/USDT P34_200

**Symbol:** ZPAY/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.5826 |
| net_win_rate | 0.4150 |
| gross_profit_factor | 0.7122 |
| gross_win_rate | 0.4150 |
| sharpe_ratio | -3.3322 |
| sortino_ratio | -0.9460 |
| max_drawdown | 0.6920 |
| cagr | -0.3557 |
| net_avg_win | 54.6881 |
| net_avg_loss | -66.6078 |
| avg_hold_time_bars | 29.4369 |
| exposure | 0.5488 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
