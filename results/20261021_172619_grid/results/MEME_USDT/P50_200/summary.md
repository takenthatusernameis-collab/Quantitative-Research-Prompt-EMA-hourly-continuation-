# EMA Hourly Continuation — MEME/USDT P50_200

**Symbol:** MEME/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 280 |
| net_profit_factor | 0.7864 |
| net_win_rate | 0.4857 |
| gross_profit_factor | 0.9394 |
| gross_win_rate | 0.4857 |
| sharpe_ratio | -1.2222 |
| sortino_ratio | -0.2918 |
| max_drawdown | 0.2984 |
| cagr | -0.1261 |
| net_avg_win | 77.7576 |
| net_avg_loss | -93.3803 |
| avg_hold_time_bars | 35.8821 |
| exposure | 0.4567 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
