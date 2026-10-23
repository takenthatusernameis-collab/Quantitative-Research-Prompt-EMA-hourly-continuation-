# EMA Hourly Continuation — AUCTION/USDT P55_144

**Symbol:** AUCTION/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 523 |
| net_profit_factor | 0.5063 |
| net_win_rate | 0.4398 |
| gross_profit_factor | 0.8253 |
| gross_win_rate | 0.4551 |
| sharpe_ratio | -5.0283 |
| sortino_ratio | -1.6120 |
| max_drawdown | 0.8661 |
| cagr | -0.5431 |
| net_avg_win | 38.3986 |
| net_avg_loss | -59.5379 |
| avg_hold_time_bars | 11.8088 |
| exposure | 0.2795 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
