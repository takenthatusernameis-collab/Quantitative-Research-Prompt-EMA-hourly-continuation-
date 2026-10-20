# EMA Hourly Continuation — CARV/USDT P34_50

**Symbol:** CARV/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 614 |
| net_profit_factor | 0.3899 |
| net_win_rate | 0.4479 |
| gross_profit_factor | 0.8389 |
| gross_win_rate | 0.4805 |
| sharpe_ratio | -7.1601 |
| sortino_ratio | -2.8022 |
| max_drawdown | 0.9396 |
| cagr | -0.7470 |
| net_avg_win | 21.8083 |
| net_avg_loss | -45.3739 |
| avg_hold_time_bars | 3.5163 |
| exposure | 0.1215 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
