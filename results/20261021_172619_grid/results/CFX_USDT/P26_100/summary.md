# EMA Hourly Continuation — CFX/USDT P26_100

**Symbol:** CFX/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.7937 |
| net_win_rate | 0.5035 |
| gross_profit_factor | 1.0040 |
| gross_win_rate | 0.5035 |
| sharpe_ratio | -1.4748 |
| sortino_ratio | -0.4345 |
| max_drawdown | 0.4190 |
| cagr | -0.1816 |
| net_avg_win | 71.4490 |
| net_avg_loss | -91.3026 |
| avg_hold_time_bars | 18.0189 |
| exposure | 0.3465 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
