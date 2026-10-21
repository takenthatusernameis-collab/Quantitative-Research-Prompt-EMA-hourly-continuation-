# EMA Hourly Continuation — IMX/USDT P21_34

**Symbol:** IMX/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 333 |
| net_profit_factor | 0.5941 |
| net_win_rate | 0.4474 |
| gross_profit_factor | 0.8101 |
| gross_win_rate | 0.4474 |
| sharpe_ratio | -2.9747 |
| sortino_ratio | -0.7719 |
| max_drawdown | 0.5966 |
| cagr | -0.2989 |
| net_avg_win | 58.1340 |
| net_avg_loss | -79.2356 |
| avg_hold_time_bars | 5.0360 |
| exposure | 0.0759 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
