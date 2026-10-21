# EMA Hourly Continuation — QI/USDT P34_89

**Symbol:** QI/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 440 |
| net_profit_factor | 0.8199 |
| net_win_rate | 0.5295 |
| gross_profit_factor | 1.1185 |
| gross_win_rate | 0.5295 |
| sharpe_ratio | -1.2871 |
| sortino_ratio | -0.3884 |
| max_drawdown | 0.4305 |
| cagr | -0.1648 |
| net_avg_win | 71.3286 |
| net_avg_loss | -97.9209 |
| avg_hold_time_bars | 10.6250 |
| exposure | 0.2115 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
