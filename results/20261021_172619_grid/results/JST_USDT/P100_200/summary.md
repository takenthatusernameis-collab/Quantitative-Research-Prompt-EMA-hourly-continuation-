# EMA Hourly Continuation — JST/USDT P100_200

**Symbol:** JST/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 276 |
| net_profit_factor | 0.6464 |
| net_win_rate | 0.5217 |
| gross_profit_factor | 1.1004 |
| gross_win_rate | 0.5254 |
| sharpe_ratio | -2.1325 |
| sortino_ratio | -0.5062 |
| max_drawdown | 0.4808 |
| cagr | -0.2102 |
| net_avg_win | 56.9513 |
| net_avg_loss | -96.1172 |
| avg_hold_time_bars | 13.4130 |
| exposure | 0.1675 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
