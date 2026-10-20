# EMA Hourly Continuation — AUCTION/USDT P12_20

**Symbol:** AUCTION/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1337 |
| net_profit_factor | 0.3333 |
| net_win_rate | 0.3844 |
| gross_profit_factor | 0.8096 |
| gross_win_rate | 0.4428 |
| sharpe_ratio | -12.9934 |
| sortino_ratio | -6.7557 |
| max_drawdown | 0.9998 |
| cagr | -0.9691 |
| net_avg_win | 9.7257 |
| net_avg_loss | -18.2229 |
| avg_hold_time_bars | 3.1085 |
| exposure | 0.1881 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
