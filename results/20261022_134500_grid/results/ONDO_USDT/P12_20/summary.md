# EMA Hourly Continuation — ONDO/USDT P12_20

**Symbol:** ONDO/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1479 |
| net_profit_factor | 0.2830 |
| net_win_rate | 0.3955 |
| gross_profit_factor | 0.6290 |
| gross_win_rate | 0.4199 |
| sharpe_ratio | -13.3361 |
| sortino_ratio | -7.3035 |
| max_drawdown | 0.9999 |
| cagr | -0.9770 |
| net_avg_win | 6.7468 |
| net_avg_loss | -15.5997 |
| avg_hold_time_bars | 2.0372 |
| exposure | 0.1370 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
