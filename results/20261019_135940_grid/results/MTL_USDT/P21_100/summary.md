# EMA Hourly Continuation — MTL/USDT P21_100

**Symbol:** MTL/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 551 |
| net_profit_factor | 0.5249 |
| net_win_rate | 0.4338 |
| gross_profit_factor | 0.8295 |
| gross_win_rate | 0.4483 |
| sharpe_ratio | -5.0056 |
| sortino_ratio | -1.6409 |
| max_drawdown | 0.8728 |
| cagr | -0.5527 |
| net_avg_win | 40.1462 |
| net_avg_loss | -58.5927 |
| avg_hold_time_bars | 19.5154 |
| exposure | 0.4866 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
