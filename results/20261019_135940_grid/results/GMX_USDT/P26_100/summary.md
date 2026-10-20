# EMA Hourly Continuation — GMX/USDT P26_100

**Symbol:** GMX/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 675 |
| net_profit_factor | 0.5944 |
| net_win_rate | 0.4578 |
| gross_profit_factor | 0.9394 |
| gross_win_rate | 0.4652 |
| sharpe_ratio | -4.7297 |
| sortino_ratio | -1.7340 |
| max_drawdown | 0.8770 |
| cagr | -0.5601 |
| net_avg_win | 41.3927 |
| net_avg_loss | -58.7952 |
| avg_hold_time_bars | 10.9644 |
| exposure | 0.3364 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
