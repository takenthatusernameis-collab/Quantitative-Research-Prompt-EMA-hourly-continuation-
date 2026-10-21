# EMA Hourly Continuation — UMA/USDT P26_89

**Symbol:** UMA/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 507 |
| net_profit_factor | 0.8015 |
| net_win_rate | 0.5148 |
| gross_profit_factor | 1.0714 |
| gross_win_rate | 0.5148 |
| sharpe_ratio | -1.7033 |
| sortino_ratio | -0.5504 |
| max_drawdown | 0.5056 |
| cagr | -0.2245 |
| net_avg_win | 72.9993 |
| net_avg_loss | -96.6306 |
| avg_hold_time_bars | 13.7337 |
| exposure | 0.3165 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
