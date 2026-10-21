# EMA Hourly Continuation — GRT/USDT P8_34

**Symbol:** GRT/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 706 |
| net_profit_factor | 0.7093 |
| net_win_rate | 0.4788 |
| gross_profit_factor | 0.9237 |
| gross_win_rate | 0.4788 |
| sharpe_ratio | -3.0119 |
| sortino_ratio | -1.1406 |
| max_drawdown | 0.7396 |
| cagr | -0.4070 |
| net_avg_win | 52.8771 |
| net_avg_loss | -68.4674 |
| avg_hold_time_bars | 8.8909 |
| exposure | 0.2840 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
