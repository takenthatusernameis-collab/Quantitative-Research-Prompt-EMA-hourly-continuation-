# EMA Hourly Continuation — OP/USDT P89_100

**Symbol:** OP/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 611 |
| net_profit_factor | 0.3042 |
| net_win_rate | 0.4026 |
| gross_profit_factor | 0.8111 |
| gross_win_rate | 0.4337 |
| sharpe_ratio | -8.8263 |
| sortino_ratio | -3.1556 |
| max_drawdown | 0.9831 |
| cagr | -0.8030 |
| net_avg_win | 17.4703 |
| net_avg_loss | -38.7087 |
| avg_hold_time_bars | 1.9476 |
| exposure | 0.0541 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
