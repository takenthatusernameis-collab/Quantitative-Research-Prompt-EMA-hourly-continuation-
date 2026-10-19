# EMA Hourly Continuation — TAO/USDT P21_50

**Symbol:** TAO/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1017 |
| net_profit_factor | 0.5734 |
| net_win_rate | 0.4661 |
| gross_profit_factor | 0.9330 |
| gross_win_rate | 0.4749 |
| sharpe_ratio | -6.4510 |
| sortino_ratio | -2.8809 |
| max_drawdown | 0.9718 |
| cagr | -0.7577 |
| net_avg_win | 27.5512 |
| net_avg_loss | -41.9425 |
| avg_hold_time_bars | 4.1681 |
| exposure | 0.1927 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
