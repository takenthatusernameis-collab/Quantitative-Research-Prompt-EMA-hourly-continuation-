# EMA Hourly Continuation — MEME/USDT P34_89

**Symbol:** MEME/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 716 |
| net_profit_factor | 0.6139 |
| net_win_rate | 0.4735 |
| gross_profit_factor | 0.9247 |
| gross_win_rate | 0.4749 |
| sharpe_ratio | -4.3946 |
| sortino_ratio | -1.6674 |
| max_drawdown | 0.8734 |
| cagr | -0.5462 |
| net_avg_win | 40.4483 |
| net_avg_loss | -59.2497 |
| avg_hold_time_bars | 7.6313 |
| exposure | 0.2484 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
