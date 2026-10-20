# EMA Hourly Continuation — EUL/USDT P8_200

**Symbol:** EUL/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 460 |
| net_profit_factor | 0.6277 |
| net_win_rate | 0.4674 |
| gross_profit_factor | 0.8651 |
| gross_win_rate | 0.4717 |
| sharpe_ratio | -2.8173 |
| sortino_ratio | -0.8503 |
| max_drawdown | 0.6614 |
| cagr | -0.3311 |
| net_avg_win | 49.8449 |
| net_avg_loss | -69.6907 |
| avg_hold_time_bars | 35.5261 |
| exposure | 0.7428 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
