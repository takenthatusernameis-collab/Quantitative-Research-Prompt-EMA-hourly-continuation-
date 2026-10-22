# EMA Hourly Continuation — OSMO/USDT P20_34

**Symbol:** OSMO/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.5381 |
| net_win_rate | 0.4138 |
| gross_profit_factor | 0.8240 |
| gross_win_rate | 0.4138 |
| sharpe_ratio | -5.0475 |
| sortino_ratio | -1.5545 |
| max_drawdown | 0.8394 |
| cagr | -0.5112 |
| net_avg_win | 50.6121 |
| net_avg_loss | -66.3980 |
| avg_hold_time_bars | 4.8815 |
| exposure | 0.1030 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
