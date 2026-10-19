# EMA Hourly Continuation — STRK/USDT P34_89

**Symbol:** STRK/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 664 |
| net_profit_factor | 0.6217 |
| net_win_rate | 0.4789 |
| gross_profit_factor | 0.9351 |
| gross_win_rate | 0.4804 |
| sharpe_ratio | -4.0936 |
| sortino_ratio | -1.4876 |
| max_drawdown | 0.8423 |
| cagr | -0.5094 |
| net_avg_win | 43.0425 |
| net_avg_loss | -63.6273 |
| avg_hold_time_bars | 7.7304 |
| exposure | 0.2333 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
