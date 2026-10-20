# EMA Hourly Continuation — GMT/USDT P21_50

**Symbol:** GMT/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1016 |
| net_profit_factor | 0.5007 |
| net_win_rate | 0.4400 |
| gross_profit_factor | 0.9028 |
| gross_win_rate | 0.4508 |
| sharpe_ratio | -7.9046 |
| sortino_ratio | -3.5476 |
| max_drawdown | 0.9880 |
| cagr | -0.8257 |
| net_avg_win | 22.1508 |
| net_avg_loss | -34.7576 |
| avg_hold_time_bars | 4.3524 |
| exposure | 0.2010 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
