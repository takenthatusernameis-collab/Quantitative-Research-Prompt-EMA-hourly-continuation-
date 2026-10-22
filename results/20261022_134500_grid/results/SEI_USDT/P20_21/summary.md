# EMA Hourly Continuation — SEI/USDT P20_21

**Symbol:** SEI/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1179 |
| net_profit_factor | 0.1738 |
| net_win_rate | 0.2833 |
| gross_profit_factor | 0.6330 |
| gross_win_rate | 0.3537 |
| sharpe_ratio | -17.8422 |
| sortino_ratio | -9.3100 |
| max_drawdown | 1.0000 |
| cagr | -0.9950 |
| net_avg_win | 6.2998 |
| net_avg_loss | -14.3244 |
| avg_hold_time_bars | 1.5852 |
| exposure | 0.0850 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
