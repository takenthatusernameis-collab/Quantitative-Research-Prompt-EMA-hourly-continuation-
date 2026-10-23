# EMA Hourly Continuation — MEME/USDT P21_50

**Symbol:** MEME/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1044 |
| net_profit_factor | 0.5189 |
| net_win_rate | 0.4473 |
| gross_profit_factor | 0.8783 |
| gross_win_rate | 0.4579 |
| sharpe_ratio | -7.0459 |
| sortino_ratio | -3.2208 |
| max_drawdown | 0.9806 |
| cagr | -0.7849 |
| net_avg_win | 22.6048 |
| net_avg_loss | -35.2611 |
| avg_hold_time_bars | 4.2893 |
| exposure | 0.2035 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
