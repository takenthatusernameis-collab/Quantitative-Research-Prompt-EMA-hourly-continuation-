# EMA Hourly Continuation — DOGS/USDT P144_200

**Symbol:** DOGS/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 0.5083 |
| net_win_rate | 0.4479 |
| gross_profit_factor | 0.8402 |
| gross_win_rate | 0.4507 |
| sharpe_ratio | -4.5395 |
| sortino_ratio | -1.3005 |
| max_drawdown | 0.7652 |
| cagr | -0.4761 |
| net_avg_win | 48.8422 |
| net_avg_loss | -77.9449 |
| avg_hold_time_bars | 4.2113 |
| exposure | 0.0793 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
