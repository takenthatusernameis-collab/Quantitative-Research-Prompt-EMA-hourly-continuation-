# EMA Hourly Continuation — POL/USDT P12_55

**Symbol:** POL/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1010 |
| net_profit_factor | 0.4198 |
| net_win_rate | 0.4386 |
| gross_profit_factor | 0.7737 |
| gross_win_rate | 0.4535 |
| sharpe_ratio | -7.8033 |
| sortino_ratio | -3.4797 |
| max_drawdown | 0.9869 |
| cagr | -0.8219 |
| net_avg_win | 16.1177 |
| net_avg_loss | -29.9980 |
| avg_hold_time_bars | 9.1911 |
| exposure | 0.4220 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
