# EMA Hourly Continuation — APT/USDT P8_34

**Symbol:** APT/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1375 |
| net_profit_factor | 0.4835 |
| net_win_rate | 0.4480 |
| gross_profit_factor | 0.8865 |
| gross_win_rate | 0.4560 |
| sharpe_ratio | -9.0201 |
| sortino_ratio | -4.6810 |
| max_drawdown | 0.9973 |
| cagr | -0.9045 |
| net_avg_win | 15.1529 |
| net_avg_loss | -25.4370 |
| avg_hold_time_bars | 5.2255 |
| exposure | 0.3266 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
