# EMA Hourly Continuation — ENA/USDT P20_34

**Symbol:** ENA/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 299 |
| net_profit_factor | 0.7927 |
| net_win_rate | 0.5084 |
| gross_profit_factor | 1.0025 |
| gross_win_rate | 0.5084 |
| sharpe_ratio | -1.0980 |
| sortino_ratio | -0.2727 |
| max_drawdown | 0.3176 |
| cagr | -0.1186 |
| net_avg_win | 68.3436 |
| net_avg_loss | -89.1470 |
| avg_hold_time_bars | 5.3913 |
| exposure | 0.0733 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
