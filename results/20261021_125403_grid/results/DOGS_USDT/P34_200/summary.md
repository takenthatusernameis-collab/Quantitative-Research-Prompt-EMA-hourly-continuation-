# EMA Hourly Continuation — DOGS/USDT P34_200

**Symbol:** DOGS/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 251 |
| net_profit_factor | 0.8012 |
| net_win_rate | 0.4861 |
| gross_profit_factor | 0.9460 |
| gross_win_rate | 0.4861 |
| sharpe_ratio | -1.2045 |
| sortino_ratio | -0.2942 |
| max_drawdown | 0.3075 |
| cagr | -0.1276 |
| net_avg_win | 84.0716 |
| net_avg_loss | -99.2404 |
| avg_hold_time_bars | 37.3147 |
| exposure | 0.4969 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
