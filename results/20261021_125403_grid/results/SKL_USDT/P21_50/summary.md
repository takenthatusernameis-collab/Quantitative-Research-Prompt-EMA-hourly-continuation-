# EMA Hourly Continuation — SKL/USDT P21_50

**Symbol:** SKL/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 512 |
| net_profit_factor | 0.6637 |
| net_win_rate | 0.4629 |
| gross_profit_factor | 0.8788 |
| gross_win_rate | 0.4629 |
| sharpe_ratio | -3.1067 |
| sortino_ratio | -1.0022 |
| max_drawdown | 0.7043 |
| cagr | -0.3684 |
| net_avg_win | 57.0085 |
| net_avg_loss | -74.0251 |
| avg_hold_time_bars | 7.3965 |
| exposure | 0.1721 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
