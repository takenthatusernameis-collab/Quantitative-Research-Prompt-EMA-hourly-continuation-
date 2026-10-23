# EMA Hourly Continuation — KSM/USDT P50_144

**Symbol:** KSM/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 490 |
| net_profit_factor | 0.6004 |
| net_win_rate | 0.4735 |
| gross_profit_factor | 0.9659 |
| gross_win_rate | 0.4837 |
| sharpe_ratio | -3.8563 |
| sortino_ratio | -1.1959 |
| max_drawdown | 0.7804 |
| cagr | -0.4405 |
| net_avg_win | 49.6988 |
| net_avg_loss | -74.4317 |
| avg_hold_time_bars | 12.0245 |
| exposure | 0.2678 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
