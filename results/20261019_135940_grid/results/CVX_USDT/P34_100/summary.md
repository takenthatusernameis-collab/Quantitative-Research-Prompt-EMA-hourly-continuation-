# EMA Hourly Continuation — CVX/USDT P34_100

**Symbol:** CVX/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 642 |
| net_profit_factor | 0.5155 |
| net_win_rate | 0.4408 |
| gross_profit_factor | 0.8021 |
| gross_win_rate | 0.4470 |
| sharpe_ratio | -5.1237 |
| sortino_ratio | -1.8051 |
| max_drawdown | 0.8952 |
| cagr | -0.5912 |
| net_avg_win | 33.6227 |
| net_avg_loss | -51.4131 |
| avg_hold_time_bars | 9.1931 |
| exposure | 0.2683 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
