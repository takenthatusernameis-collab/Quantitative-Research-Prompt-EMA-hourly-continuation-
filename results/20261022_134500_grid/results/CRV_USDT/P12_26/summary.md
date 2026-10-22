# EMA Hourly Continuation — CRV/USDT P12_26

**Symbol:** CRV/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1387 |
| net_profit_factor | 0.4262 |
| net_win_rate | 0.4614 |
| gross_profit_factor | 0.8849 |
| gross_win_rate | 0.4795 |
| sharpe_ratio | -9.1885 |
| sortino_ratio | -4.8011 |
| max_drawdown | 0.9977 |
| cagr | -0.9106 |
| net_avg_win | 11.5777 |
| net_avg_loss | -23.2751 |
| avg_hold_time_bars | 2.9380 |
| exposure | 0.1852 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
