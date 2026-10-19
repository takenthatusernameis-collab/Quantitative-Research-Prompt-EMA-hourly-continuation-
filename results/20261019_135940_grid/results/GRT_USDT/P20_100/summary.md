# EMA Hourly Continuation — GRT/USDT P20_100

**Symbol:** GRT/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 658 |
| net_profit_factor | 0.6114 |
| net_win_rate | 0.4650 |
| gross_profit_factor | 0.8764 |
| gross_win_rate | 0.4696 |
| sharpe_ratio | -4.0863 |
| sortino_ratio | -1.4748 |
| max_drawdown | 0.8388 |
| cagr | -0.5042 |
| net_avg_win | 42.6642 |
| net_avg_loss | -60.6578 |
| avg_hold_time_bars | 13.5167 |
| exposure | 0.4025 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
