# EMA Hourly Continuation — BOME/USDT P12_55

**Symbol:** BOME/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 619 |
| net_profit_factor | 0.7547 |
| net_win_rate | 0.4733 |
| gross_profit_factor | 0.9097 |
| gross_win_rate | 0.4733 |
| sharpe_ratio | -2.3588 |
| sortino_ratio | -0.8355 |
| max_drawdown | 0.6630 |
| cagr | -0.3200 |
| net_avg_win | 65.1489 |
| net_avg_loss | -77.5829 |
| avg_hold_time_bars | 11.5137 |
| exposure | 0.3240 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
