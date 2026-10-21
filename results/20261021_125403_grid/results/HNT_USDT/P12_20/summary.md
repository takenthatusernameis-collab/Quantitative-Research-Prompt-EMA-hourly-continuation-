# EMA Hourly Continuation — HNT/USDT P12_20

**Symbol:** HNT/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 288 |
| net_profit_factor | 0.4964 |
| net_win_rate | 0.3993 |
| gross_profit_factor | 0.6794 |
| gross_win_rate | 0.3993 |
| sharpe_ratio | -3.8260 |
| sortino_ratio | -0.9215 |
| max_drawdown | 0.6617 |
| cagr | -0.3463 |
| net_avg_win | 56.2355 |
| net_avg_loss | -75.3084 |
| avg_hold_time_bars | 6.3160 |
| exposure | 0.0827 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
