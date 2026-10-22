# EMA Hourly Continuation — CVX/USDT P89_200

**Symbol:** CVX/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.5435 |
| net_win_rate | 0.4392 |
| gross_profit_factor | 0.7725 |
| gross_win_rate | 0.4392 |
| sharpe_ratio | -3.6305 |
| sortino_ratio | -0.9762 |
| max_drawdown | 0.6880 |
| cagr | -0.3712 |
| net_avg_win | 51.5290 |
| net_avg_loss | -74.2541 |
| avg_hold_time_bars | 11.0497 |
| exposure | 0.1818 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
