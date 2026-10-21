# EMA Hourly Continuation — APE/USDT P26_55

**Symbol:** APE/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.7149 |
| net_win_rate | 0.4903 |
| gross_profit_factor | 0.9620 |
| gross_win_rate | 0.4903 |
| sharpe_ratio | -2.1480 |
| sortino_ratio | -0.6247 |
| max_drawdown | 0.5288 |
| cagr | -0.2481 |
| net_avg_win | 63.4626 |
| net_avg_loss | -85.3913 |
| avg_hold_time_bars | 6.4199 |
| exposure | 0.1202 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
