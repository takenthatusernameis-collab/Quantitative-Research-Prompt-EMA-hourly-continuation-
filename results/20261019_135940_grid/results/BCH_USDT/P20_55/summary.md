# EMA Hourly Continuation — BCH/USDT P20_55

**Symbol:** BCH/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 917 |
| net_profit_factor | 0.3669 |
| net_win_rate | 0.4220 |
| gross_profit_factor | 0.7725 |
| gross_win_rate | 0.4438 |
| sharpe_ratio | -9.1368 |
| sortino_ratio | -3.9288 |
| max_drawdown | 0.9930 |
| cagr | -0.8606 |
| net_avg_win | 14.8658 |
| net_avg_loss | -29.5890 |
| avg_hold_time_bars | 6.1581 |
| exposure | 0.2567 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
