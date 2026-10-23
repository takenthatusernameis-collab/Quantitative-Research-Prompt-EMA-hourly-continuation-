# EMA Hourly Continuation — HNT/USDT P21_55

**Symbol:** HNT/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1007 |
| net_profit_factor | 0.5021 |
| net_win_rate | 0.4419 |
| gross_profit_factor | 0.8206 |
| gross_win_rate | 0.4479 |
| sharpe_ratio | -7.1045 |
| sortino_ratio | -3.1790 |
| max_drawdown | 0.9800 |
| cagr | -0.7852 |
| net_avg_win | 22.1842 |
| net_avg_loss | -34.9856 |
| avg_hold_time_bars | 5.1003 |
| exposure | 0.2335 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
