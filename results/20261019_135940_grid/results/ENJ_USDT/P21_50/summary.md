# EMA Hourly Continuation — ENJ/USDT P21_50

**Symbol:** ENJ/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 995 |
| net_profit_factor | 0.4901 |
| net_win_rate | 0.4492 |
| gross_profit_factor | 0.9206 |
| gross_win_rate | 0.4633 |
| sharpe_ratio | -7.6391 |
| sortino_ratio | -3.4062 |
| max_drawdown | 0.9853 |
| cagr | -0.8119 |
| net_avg_win | 21.1756 |
| net_avg_loss | -35.2463 |
| avg_hold_time_bars | 4.3166 |
| exposure | 0.1952 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
