# EMA Hourly Continuation — MLK/USDT P55_200

**Symbol:** MLK/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 539 |
| net_profit_factor | 0.3584 |
| net_win_rate | 0.3210 |
| gross_profit_factor | 0.5735 |
| gross_win_rate | 0.3247 |
| sharpe_ratio | -8.2604 |
| sortino_ratio | -2.7092 |
| max_drawdown | 0.9680 |
| cagr | -0.7425 |
| net_avg_win | 31.2339 |
| net_avg_loss | -41.1943 |
| avg_hold_time_bars | 14.5028 |
| exposure | 0.3538 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
