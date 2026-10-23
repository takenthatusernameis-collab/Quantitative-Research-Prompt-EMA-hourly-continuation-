# EMA Hourly Continuation — SYN/USDT P12_200

**Symbol:** SYN/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 410 |
| net_profit_factor | 0.6905 |
| net_win_rate | 0.4805 |
| gross_profit_factor | 0.9029 |
| gross_win_rate | 0.4854 |
| sharpe_ratio | -2.0443 |
| sortino_ratio | -0.5854 |
| max_drawdown | 0.5370 |
| cagr | -0.2416 |
| net_avg_win | 56.6873 |
| net_avg_loss | -75.9341 |
| avg_hold_time_bars | 39.6659 |
| exposure | 0.7392 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
