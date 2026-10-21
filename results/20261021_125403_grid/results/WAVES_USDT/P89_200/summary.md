# EMA Hourly Continuation — WAVES/USDT P89_200

**Symbol:** WAVES/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 309 |
| net_profit_factor | 0.6371 |
| net_win_rate | 0.4595 |
| gross_profit_factor | 0.8309 |
| gross_win_rate | 0.4595 |
| sharpe_ratio | -2.3924 |
| sortino_ratio | -0.5984 |
| max_drawdown | 0.5151 |
| cagr | -0.2414 |
| net_avg_win | 61.8491 |
| net_avg_loss | -82.5505 |
| avg_hold_time_bars | 13.3010 |
| exposure | 0.1868 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
