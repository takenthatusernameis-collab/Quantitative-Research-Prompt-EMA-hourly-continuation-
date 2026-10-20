# EMA Hourly Continuation — SWFTC/USDT P20_50

**Symbol:** SWFTC/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 939 |
| net_profit_factor | 0.3727 |
| net_win_rate | 0.3951 |
| gross_profit_factor | 0.6837 |
| gross_win_rate | 0.4079 |
| sharpe_ratio | -9.4169 |
| sortino_ratio | -4.0668 |
| max_drawdown | 0.9944 |
| cagr | -0.8726 |
| net_avg_win | 15.9228 |
| net_avg_loss | -27.9063 |
| avg_hold_time_bars | 4.8658 |
| exposure | 0.2077 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
