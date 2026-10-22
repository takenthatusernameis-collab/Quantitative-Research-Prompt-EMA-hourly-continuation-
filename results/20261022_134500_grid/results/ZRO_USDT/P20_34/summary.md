# EMA Hourly Continuation — ZRO/USDT P20_34

**Symbol:** ZRO/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1120 |
| net_profit_factor | 0.4943 |
| net_win_rate | 0.4420 |
| gross_profit_factor | 0.9299 |
| gross_win_rate | 0.4571 |
| sharpe_ratio | -8.8264 |
| sortino_ratio | -4.3254 |
| max_drawdown | 0.9933 |
| cagr | -0.8824 |
| net_avg_win | 19.6127 |
| net_avg_loss | -31.4245 |
| avg_hold_time_bars | 2.5955 |
| exposure | 0.1423 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
