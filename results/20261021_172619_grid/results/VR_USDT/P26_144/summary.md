# EMA Hourly Continuation — VR/USDT P26_144

**Symbol:** VR/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.5789 |
| net_win_rate | 0.4149 |
| gross_profit_factor | 0.6917 |
| gross_win_rate | 0.4149 |
| sharpe_ratio | -3.0338 |
| sortino_ratio | -0.7808 |
| max_drawdown | 0.5988 |
| cagr | -0.3049 |
| net_avg_win | 59.2188 |
| net_avg_loss | -72.5461 |
| avg_hold_time_bars | 26.9433 |
| exposure | 0.4103 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
