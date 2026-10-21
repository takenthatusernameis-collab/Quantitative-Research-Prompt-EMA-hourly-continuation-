# EMA Hourly Continuation — GRT/USDT P12_50

**Symbol:** GRT/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 635 |
| net_profit_factor | 0.8095 |
| net_win_rate | 0.5039 |
| gross_profit_factor | 1.0349 |
| gross_win_rate | 0.5039 |
| sharpe_ratio | -1.9542 |
| sortino_ratio | -0.7049 |
| max_drawdown | 0.6757 |
| cagr | -0.2773 |
| net_avg_win | 74.2400 |
| net_avg_loss | -93.1705 |
| avg_hold_time_bars | 10.7858 |
| exposure | 0.3099 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
