# EMA Hourly Continuation — TWT/USDT P34_89

**Symbol:** TWT/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 468 |
| net_profit_factor | 0.6777 |
| net_win_rate | 0.4893 |
| gross_profit_factor | 0.9666 |
| gross_win_rate | 0.4893 |
| sharpe_ratio | -2.6972 |
| sortino_ratio | -0.8357 |
| max_drawdown | 0.6340 |
| cagr | -0.3184 |
| net_avg_win | 56.7504 |
| net_avg_loss | -80.2382 |
| avg_hold_time_bars | 10.9338 |
| exposure | 0.2326 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
