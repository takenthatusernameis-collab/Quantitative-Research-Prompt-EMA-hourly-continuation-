# EMA Hourly Continuation — RSR/USDT P20_34

**Symbol:** RSR/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1093 |
| net_profit_factor | 0.4062 |
| net_win_rate | 0.4346 |
| gross_profit_factor | 0.7965 |
| gross_win_rate | 0.4437 |
| sharpe_ratio | -8.9511 |
| sortino_ratio | -4.2071 |
| max_drawdown | 0.9944 |
| cagr | -0.8721 |
| net_avg_win | 14.3215 |
| net_avg_loss | -27.0963 |
| avg_hold_time_bars | 2.8948 |
| exposure | 0.1438 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
