# EMA Hourly Continuation — COMP/USDT P12_26

**Symbol:** COMP/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 588 |
| net_profit_factor | 0.5495 |
| net_win_rate | 0.4507 |
| gross_profit_factor | 0.8183 |
| gross_win_rate | 0.4507 |
| sharpe_ratio | -4.6440 |
| sortino_ratio | -1.6126 |
| max_drawdown | 0.8490 |
| cagr | -0.5237 |
| net_avg_win | 38.8879 |
| net_avg_loss | -58.0573 |
| avg_hold_time_bars | 5.7398 |
| exposure | 0.1534 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
