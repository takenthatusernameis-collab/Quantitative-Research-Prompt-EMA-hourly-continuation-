# EMA Hourly Continuation — WOO/USDT P89_200

**Symbol:** WOO/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 360 |
| net_profit_factor | 0.6123 |
| net_win_rate | 0.4667 |
| gross_profit_factor | 0.8648 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -2.8563 |
| sortino_ratio | -0.7703 |
| max_drawdown | 0.5936 |
| cagr | -0.3013 |
| net_avg_win | 55.7953 |
| net_avg_loss | -79.7363 |
| avg_hold_time_bars | 11.6694 |
| exposure | 0.1910 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
