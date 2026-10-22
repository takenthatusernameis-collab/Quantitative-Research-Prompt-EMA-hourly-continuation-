# EMA Hourly Continuation — GMT/USDT P12_55

**Symbol:** GMT/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 604 |
| net_profit_factor | 0.7606 |
| net_win_rate | 0.4967 |
| gross_profit_factor | 0.9792 |
| gross_win_rate | 0.4967 |
| sharpe_ratio | -2.0525 |
| sortino_ratio | -0.7226 |
| max_drawdown | 0.5809 |
| cagr | -0.2824 |
| net_avg_win | 59.8692 |
| net_avg_loss | -77.6808 |
| avg_hold_time_bars | 13.5911 |
| exposure | 0.3731 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
