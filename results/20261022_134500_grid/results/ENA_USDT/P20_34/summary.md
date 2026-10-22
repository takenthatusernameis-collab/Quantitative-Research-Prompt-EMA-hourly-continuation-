# EMA Hourly Continuation — ENA/USDT P20_34

**Symbol:** ENA/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1164 |
| net_profit_factor | 0.4589 |
| net_win_rate | 0.4527 |
| gross_profit_factor | 0.7796 |
| gross_win_rate | 0.4596 |
| sharpe_ratio | -7.7076 |
| sortino_ratio | -3.7246 |
| max_drawdown | 0.9899 |
| cagr | -0.8349 |
| net_avg_win | 15.9192 |
| net_avg_loss | -28.6985 |
| avg_hold_time_bars | 2.6143 |
| exposure | 0.1383 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
