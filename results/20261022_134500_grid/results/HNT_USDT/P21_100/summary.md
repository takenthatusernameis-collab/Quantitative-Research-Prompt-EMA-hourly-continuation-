# EMA Hourly Continuation — HNT/USDT P21_100

**Symbol:** HNT/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 700 |
| net_profit_factor | 0.5440 |
| net_win_rate | 0.4443 |
| gross_profit_factor | 0.7770 |
| gross_win_rate | 0.4486 |
| sharpe_ratio | -4.7911 |
| sortino_ratio | -1.7864 |
| max_drawdown | 0.8898 |
| cagr | -0.5731 |
| net_avg_win | 33.8335 |
| net_avg_loss | -49.7238 |
| avg_hold_time_bars | 13.0029 |
| exposure | 0.4137 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
