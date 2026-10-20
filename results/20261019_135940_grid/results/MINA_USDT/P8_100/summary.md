# EMA Hourly Continuation — MINA/USDT P8_100

**Symbol:** MINA/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 663 |
| net_profit_factor | 0.6723 |
| net_win_rate | 0.4917 |
| gross_profit_factor | 0.9896 |
| gross_win_rate | 0.5023 |
| sharpe_ratio | -3.1080 |
| sortino_ratio | -1.1203 |
| max_drawdown | 0.7738 |
| cagr | -0.4184 |
| net_avg_win | 46.8008 |
| net_avg_loss | -67.3371 |
| avg_hold_time_bars | 22.3605 |
| exposure | 0.6739 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
