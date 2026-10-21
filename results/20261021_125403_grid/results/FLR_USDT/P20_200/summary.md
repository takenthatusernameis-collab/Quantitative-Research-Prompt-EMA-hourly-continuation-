# EMA Hourly Continuation — FLR/USDT P20_200

**Symbol:** FLR/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.7991 |
| net_win_rate | 0.5050 |
| gross_profit_factor | 1.0090 |
| gross_win_rate | 0.5075 |
| sharpe_ratio | -1.3118 |
| sortino_ratio | -0.3759 |
| max_drawdown | 0.3704 |
| cagr | -0.1597 |
| net_avg_win | 69.6987 |
| net_avg_loss | -88.9869 |
| avg_hold_time_bars | 31.1150 |
| exposure | 0.5657 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
