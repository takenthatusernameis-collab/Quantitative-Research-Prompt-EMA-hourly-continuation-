# EMA Hourly Continuation — CRO/USDT P26_89

**Symbol:** CRO/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 711 |
| net_profit_factor | 0.4226 |
| net_win_rate | 0.4318 |
| gross_profit_factor | 0.8948 |
| gross_win_rate | 0.4571 |
| sharpe_ratio | -7.1326 |
| sortino_ratio | -2.6713 |
| max_drawdown | 0.9697 |
| cagr | -0.7418 |
| net_avg_win | 23.0480 |
| net_avg_loss | -41.4407 |
| avg_hold_time_bars | 10.4051 |
| exposure | 0.3363 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
