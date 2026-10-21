# EMA Hourly Continuation — XRP/USDT P21_50

**Symbol:** XRP/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.6443 |
| net_win_rate | 0.4927 |
| gross_profit_factor | 0.9868 |
| gross_win_rate | 0.4927 |
| sharpe_ratio | -2.8657 |
| sortino_ratio | -0.8355 |
| max_drawdown | 0.6312 |
| cagr | -0.3172 |
| net_avg_win | 55.0156 |
| net_avg_loss | -82.9304 |
| avg_hold_time_bars | 7.5340 |
| exposure | 0.1411 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
