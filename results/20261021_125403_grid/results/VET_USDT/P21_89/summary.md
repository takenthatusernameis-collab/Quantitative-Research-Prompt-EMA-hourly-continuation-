# EMA Hourly Continuation — VET/USDT P21_89

**Symbol:** VET/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 510 |
| net_profit_factor | 0.8423 |
| net_win_rate | 0.5235 |
| gross_profit_factor | 1.0922 |
| gross_win_rate | 0.5235 |
| sharpe_ratio | -1.2249 |
| sortino_ratio | -0.3982 |
| max_drawdown | 0.4131 |
| cagr | -0.1694 |
| net_avg_win | 74.5453 |
| net_avg_loss | -97.2420 |
| avg_hold_time_bars | 14.7706 |
| exposure | 0.3424 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
