# EMA Hourly Continuation — AUCTION/USDT P34_89

**Symbol:** AUCTION/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 707 |
| net_profit_factor | 0.5548 |
| net_win_rate | 0.4583 |
| gross_profit_factor | 0.9220 |
| gross_win_rate | 0.4752 |
| sharpe_ratio | -5.4063 |
| sortino_ratio | -2.0291 |
| max_drawdown | 0.9154 |
| cagr | -0.6198 |
| net_avg_win | 35.1024 |
| net_avg_loss | -53.5272 |
| avg_hold_time_bars | 8.1216 |
| exposure | 0.2599 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
