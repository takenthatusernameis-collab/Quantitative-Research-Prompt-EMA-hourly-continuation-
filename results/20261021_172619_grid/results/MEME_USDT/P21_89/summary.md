# EMA Hourly Continuation — MEME/USDT P21_89

**Symbol:** MEME/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 488 |
| net_profit_factor | 0.8384 |
| net_win_rate | 0.5102 |
| gross_profit_factor | 1.0439 |
| gross_win_rate | 0.5102 |
| sharpe_ratio | -1.3062 |
| sortino_ratio | -0.4140 |
| max_drawdown | 0.4535 |
| cagr | -0.1757 |
| net_avg_win | 80.1166 |
| net_avg_loss | -99.5513 |
| avg_hold_time_bars | 17.6086 |
| exposure | 0.3906 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
