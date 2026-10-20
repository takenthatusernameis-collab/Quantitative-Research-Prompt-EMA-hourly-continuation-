# EMA Hourly Continuation — MEME/USDT P50_55

**Symbol:** MEME/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 857 |
| net_profit_factor | 0.2209 |
| net_win_rate | 0.3769 |
| gross_profit_factor | 0.6266 |
| gross_win_rate | 0.4177 |
| sharpe_ratio | -11.5162 |
| sortino_ratio | -4.8788 |
| max_drawdown | 0.9985 |
| cagr | -0.9249 |
| net_avg_win | 8.7649 |
| net_avg_loss | -24.0001 |
| avg_hold_time_bars | 1.9358 |
| exposure | 0.0754 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
