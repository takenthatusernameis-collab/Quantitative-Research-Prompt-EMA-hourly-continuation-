# EMA Hourly Continuation — KCS/USDT P20_34

**Symbol:** KCS/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1154 |
| net_profit_factor | 0.1095 |
| net_win_rate | 0.2418 |
| gross_profit_factor | 0.6159 |
| gross_win_rate | 0.3605 |
| sharpe_ratio | -19.2110 |
| sortino_ratio | -10.3000 |
| max_drawdown | 1.0000 |
| cagr | -0.9965 |
| net_avg_win | 4.4082 |
| net_avg_loss | -12.8341 |
| avg_hold_time_bars | 3.0381 |
| exposure | 0.1594 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
