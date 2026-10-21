# EMA Hourly Continuation — IOTA/USDT P20_200

**Symbol:** IOTA/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 278 |
| net_profit_factor | 0.9061 |
| net_win_rate | 0.5216 |
| gross_profit_factor | 1.0881 |
| gross_win_rate | 0.5216 |
| sharpe_ratio | -0.4788 |
| sortino_ratio | -0.1148 |
| max_drawdown | 0.1792 |
| cagr | -0.0545 |
| net_avg_win | 87.2748 |
| net_avg_loss | -105.0142 |
| avg_hold_time_bars | 50.2446 |
| exposure | 0.6349 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
