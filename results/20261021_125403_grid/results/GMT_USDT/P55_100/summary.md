# EMA Hourly Continuation — GMT/USDT P55_100

**Symbol:** GMT/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.7853 |
| net_win_rate | 0.5118 |
| gross_profit_factor | 1.0629 |
| gross_win_rate | 0.5118 |
| sharpe_ratio | -1.4796 |
| sortino_ratio | -0.3925 |
| max_drawdown | 0.4397 |
| cagr | -0.1650 |
| net_avg_win | 76.5730 |
| net_avg_loss | -102.2032 |
| avg_hold_time_bars | 7.6353 |
| exposure | 0.1180 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
