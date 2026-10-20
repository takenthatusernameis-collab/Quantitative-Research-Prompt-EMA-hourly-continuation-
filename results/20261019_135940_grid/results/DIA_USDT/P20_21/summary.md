# EMA Hourly Continuation — DIA/USDT P20_21

**Symbol:** DIA/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1177 |
| net_profit_factor | 0.1185 |
| net_win_rate | 0.3339 |
| gross_profit_factor | 0.6327 |
| gross_win_rate | 0.4308 |
| sharpe_ratio | -15.5987 |
| sortino_ratio | -7.8886 |
| max_drawdown | 1.0000 |
| cagr | -0.9868 |
| net_avg_win | 3.4199 |
| net_avg_loss | -14.4692 |
| avg_hold_time_bars | 2.0255 |
| exposure | 0.1079 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
