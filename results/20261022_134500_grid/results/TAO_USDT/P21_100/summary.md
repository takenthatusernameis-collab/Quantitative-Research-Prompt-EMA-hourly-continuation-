# EMA Hourly Continuation — TAO/USDT P21_100

**Symbol:** TAO/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 699 |
| net_profit_factor | 0.7009 |
| net_win_rate | 0.4850 |
| gross_profit_factor | 0.9754 |
| gross_win_rate | 0.4864 |
| sharpe_ratio | -3.6918 |
| sortino_ratio | -1.3639 |
| max_drawdown | 0.8234 |
| cagr | -0.4855 |
| net_avg_win | 56.1054 |
| net_avg_loss | -75.3765 |
| avg_hold_time_bars | 12.0515 |
| exposure | 0.3829 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
