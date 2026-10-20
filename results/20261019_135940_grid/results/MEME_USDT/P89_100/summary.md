# EMA Hourly Continuation — MEME/USDT P89_100

**Symbol:** MEME/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 626 |
| net_profit_factor | 0.3371 |
| net_win_rate | 0.4137 |
| gross_profit_factor | 0.8032 |
| gross_win_rate | 0.4425 |
| sharpe_ratio | -8.3593 |
| sortino_ratio | -2.9955 |
| max_drawdown | 0.9795 |
| cagr | -0.7874 |
| net_avg_win | 19.2343 |
| net_avg_loss | -40.2643 |
| avg_hold_time_bars | 2.5543 |
| exposure | 0.0727 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
