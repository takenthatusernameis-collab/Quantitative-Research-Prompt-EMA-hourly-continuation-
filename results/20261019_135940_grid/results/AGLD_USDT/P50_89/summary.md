# EMA Hourly Continuation — AGLD/USDT P50_89

**Symbol:** AGLD/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 688 |
| net_profit_factor | 0.5258 |
| net_win_rate | 0.4433 |
| gross_profit_factor | 0.8863 |
| gross_win_rate | 0.4520 |
| sharpe_ratio | -5.8198 |
| sortino_ratio | -2.1482 |
| max_drawdown | 0.9317 |
| cagr | -0.6454 |
| net_avg_win | 33.6966 |
| net_avg_loss | -51.0335 |
| avg_hold_time_bars | 5.2108 |
| exposure | 0.1622 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
