# EMA Hourly Continuation — W/USDT P21_26

**Symbol:** W/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 195 |
| net_profit_factor | 0.6716 |
| net_win_rate | 0.4718 |
| gross_profit_factor | 0.9040 |
| gross_win_rate | 0.4718 |
| sharpe_ratio | -1.8283 |
| sortino_ratio | -0.3649 |
| max_drawdown | 0.3944 |
| cagr | -0.1549 |
| net_avg_win | 76.6104 |
| net_avg_loss | -101.8900 |
| avg_hold_time_bars | 4.8154 |
| exposure | 0.0427 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
