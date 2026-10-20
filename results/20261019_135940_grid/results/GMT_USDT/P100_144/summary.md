# EMA Hourly Continuation — GMT/USDT P100_144

**Symbol:** GMT/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 506 |
| net_profit_factor | 0.4913 |
| net_win_rate | 0.4684 |
| gross_profit_factor | 0.9520 |
| gross_win_rate | 0.4802 |
| sharpe_ratio | -4.9269 |
| sortino_ratio | -1.5777 |
| max_drawdown | 0.8532 |
| cagr | -0.5309 |
| net_avg_win | 34.6600 |
| net_avg_loss | -62.1550 |
| avg_hold_time_bars | 3.8202 |
| exposure | 0.0879 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
