# EMA Hourly Continuation — ORDI/USDT P12_55

**Symbol:** ORDI/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1082 |
| net_profit_factor | 0.6764 |
| net_win_rate | 0.4797 |
| gross_profit_factor | 1.0354 |
| gross_win_rate | 0.4880 |
| sharpe_ratio | -5.1296 |
| sortino_ratio | -2.3767 |
| max_drawdown | 0.9431 |
| cagr | -0.6776 |
| net_avg_win | 37.9290 |
| net_avg_loss | -51.6919 |
| avg_hold_time_bars | 7.4464 |
| exposure | 0.3662 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
