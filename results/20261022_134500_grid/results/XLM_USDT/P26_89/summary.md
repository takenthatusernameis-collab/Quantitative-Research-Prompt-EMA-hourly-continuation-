# EMA Hourly Continuation — XLM/USDT P26_89

**Symbol:** XLM/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 698 |
| net_profit_factor | 0.4894 |
| net_win_rate | 0.4914 |
| gross_profit_factor | 1.0212 |
| gross_win_rate | 0.5043 |
| sharpe_ratio | -4.9860 |
| sortino_ratio | -1.8374 |
| max_drawdown | 0.9046 |
| cagr | -0.5984 |
| net_avg_win | 25.1207 |
| net_avg_loss | -49.5918 |
| avg_hold_time_bars | 10.3797 |
| exposure | 0.3293 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
