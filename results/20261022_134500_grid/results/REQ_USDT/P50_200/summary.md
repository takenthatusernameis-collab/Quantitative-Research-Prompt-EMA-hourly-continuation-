# EMA Hourly Continuation — REQ/USDT P50_200

**Symbol:** REQ/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 550 |
| net_profit_factor | 0.4309 |
| net_win_rate | 0.3855 |
| gross_profit_factor | 0.8170 |
| gross_win_rate | 0.4036 |
| sharpe_ratio | -7.1833 |
| sortino_ratio | -2.3800 |
| max_drawdown | 0.9512 |
| cagr | -0.6944 |
| net_avg_win | 33.8902 |
| net_avg_loss | -49.3354 |
| avg_hold_time_bars | 13.7655 |
| exposure | 0.3441 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
