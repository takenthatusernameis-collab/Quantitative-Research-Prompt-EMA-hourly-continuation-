# EMA Hourly Continuation — RLC/USDT P50_55

**Symbol:** RLC/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 821 |
| net_profit_factor | 0.2550 |
| net_win_rate | 0.3825 |
| gross_profit_factor | 0.8208 |
| gross_win_rate | 0.4458 |
| sharpe_ratio | -11.3031 |
| sortino_ratio | -4.6895 |
| max_drawdown | 0.9983 |
| cagr | -0.9207 |
| net_avg_win | 10.8829 |
| net_avg_loss | -26.4301 |
| avg_hold_time_bars | 2.5091 |
| exposure | 0.0936 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
