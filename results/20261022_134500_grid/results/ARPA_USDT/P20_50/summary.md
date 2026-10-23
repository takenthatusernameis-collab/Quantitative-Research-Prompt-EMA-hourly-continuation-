# EMA Hourly Continuation — ARPA/USDT P20_50

**Symbol:** ARPA/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1041 |
| net_profit_factor | 0.5032 |
| net_win_rate | 0.4284 |
| gross_profit_factor | 0.8863 |
| gross_win_rate | 0.4582 |
| sharpe_ratio | -8.2544 |
| sortino_ratio | -3.7733 |
| max_drawdown | 0.9901 |
| cagr | -0.8371 |
| net_avg_win | 22.4740 |
| net_avg_loss | -33.4801 |
| avg_hold_time_bars | 5.2709 |
| exposure | 0.2483 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
