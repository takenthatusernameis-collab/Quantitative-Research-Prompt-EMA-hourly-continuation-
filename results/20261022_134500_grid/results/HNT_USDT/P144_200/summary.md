# EMA Hourly Continuation — HNT/USDT P144_200

**Symbol:** HNT/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.4840 |
| net_win_rate | 0.4350 |
| gross_profit_factor | 0.7656 |
| gross_win_rate | 0.4395 |
| sharpe_ratio | -4.6300 |
| sortino_ratio | -1.3841 |
| max_drawdown | 0.8258 |
| cagr | -0.4848 |
| net_avg_win | 39.1972 |
| net_avg_loss | -62.3526 |
| avg_hold_time_bars | 4.7848 |
| exposure | 0.0970 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
