# EMA Hourly Continuation — STRAX/USDT P12_20

**Symbol:** STRAX/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 560 |
| net_profit_factor | 0.4287 |
| net_win_rate | 0.4286 |
| gross_profit_factor | 0.6833 |
| gross_win_rate | 0.4286 |
| sharpe_ratio | -5.5978 |
| sortino_ratio | -1.8999 |
| max_drawdown | 0.8911 |
| cagr | -0.5857 |
| net_avg_win | 27.7973 |
| net_avg_loss | -48.6356 |
| avg_hold_time_bars | 6.0179 |
| exposure | 0.1541 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
