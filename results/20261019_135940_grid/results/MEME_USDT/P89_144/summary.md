# EMA Hourly Continuation — MEME/USDT P89_144

**Symbol:** MEME/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 516 |
| net_profit_factor | 0.5566 |
| net_win_rate | 0.4748 |
| gross_profit_factor | 0.8952 |
| gross_win_rate | 0.4787 |
| sharpe_ratio | -4.1407 |
| sortino_ratio | -1.3156 |
| max_drawdown | 0.8066 |
| cagr | -0.4777 |
| net_avg_win | 41.2079 |
| net_avg_loss | -66.9316 |
| avg_hold_time_bars | 5.5407 |
| exposure | 0.1300 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
