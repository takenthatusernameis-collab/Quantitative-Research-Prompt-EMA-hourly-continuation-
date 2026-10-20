# EMA Hourly Continuation — ZRX/USDT P34_50

**Symbol:** ZRX/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 914 |
| net_profit_factor | 0.3394 |
| net_win_rate | 0.4059 |
| gross_profit_factor | 0.7658 |
| gross_win_rate | 0.4333 |
| sharpe_ratio | -9.6156 |
| sortino_ratio | -4.1231 |
| max_drawdown | 0.9946 |
| cagr | -0.8745 |
| net_avg_win | 13.7730 |
| net_avg_loss | -27.7261 |
| avg_hold_time_bars | 3.5328 |
| exposure | 0.1468 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
