# EMA Hourly Continuation — BCH/USDT P100_200

**Symbol:** BCH/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 277 |
| net_profit_factor | 0.7370 |
| net_win_rate | 0.5090 |
| gross_profit_factor | 1.0237 |
| gross_win_rate | 0.5090 |
| sharpe_ratio | -1.5339 |
| sortino_ratio | -0.3672 |
| max_drawdown | 0.3607 |
| cagr | -0.1542 |
| net_avg_win | 68.2255 |
| net_avg_loss | -95.9793 |
| avg_hold_time_bars | 11.1155 |
| exposure | 0.1400 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
