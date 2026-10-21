# EMA Hourly Continuation — INJ/USDT P8_100

**Symbol:** INJ/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 454 |
| net_profit_factor | 0.7778 |
| net_win_rate | 0.4780 |
| gross_profit_factor | 0.9134 |
| gross_win_rate | 0.4780 |
| sharpe_ratio | -1.6897 |
| sortino_ratio | -0.5125 |
| max_drawdown | 0.4586 |
| cagr | -0.2113 |
| net_avg_win | 72.4415 |
| net_avg_loss | -85.2724 |
| avg_hold_time_bars | 32.1145 |
| exposure | 0.6627 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
