# EMA Hourly Continuation — JUP/USDT P26_34

**Symbol:** JUP/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 177 |
| net_profit_factor | 0.7229 |
| net_win_rate | 0.4972 |
| gross_profit_factor | 0.9740 |
| gross_win_rate | 0.4972 |
| sharpe_ratio | -1.2981 |
| sortino_ratio | -0.2479 |
| max_drawdown | 0.2678 |
| cagr | -0.1074 |
| net_avg_win | 73.5803 |
| net_avg_loss | -100.6371 |
| avg_hold_time_bars | 6.0904 |
| exposure | 0.0490 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
