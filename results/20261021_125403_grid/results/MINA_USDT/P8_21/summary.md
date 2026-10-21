# EMA Hourly Continuation — MINA/USDT P8_21

**Symbol:** MINA/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 687 |
| net_profit_factor | 0.7290 |
| net_win_rate | 0.5167 |
| gross_profit_factor | 1.0376 |
| gross_win_rate | 0.5167 |
| sharpe_ratio | -2.4762 |
| sortino_ratio | -0.9340 |
| max_drawdown | 0.7091 |
| cagr | -0.3480 |
| net_avg_win | 49.8916 |
| net_avg_loss | -73.1797 |
| avg_hold_time_bars | 5.5881 |
| exposure | 0.1745 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
