# EMA Hourly Continuation — INJ/USDT P12_55

**Symbol:** INJ/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1054 |
| net_profit_factor | 0.6201 |
| net_win_rate | 0.4668 |
| gross_profit_factor | 0.9345 |
| gross_win_rate | 0.4715 |
| sharpe_ratio | -5.6715 |
| sortino_ratio | -2.5883 |
| max_drawdown | 0.9571 |
| cagr | -0.7125 |
| net_avg_win | 31.7243 |
| net_avg_loss | -44.7888 |
| avg_hold_time_bars | 7.7476 |
| exposure | 0.3712 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
