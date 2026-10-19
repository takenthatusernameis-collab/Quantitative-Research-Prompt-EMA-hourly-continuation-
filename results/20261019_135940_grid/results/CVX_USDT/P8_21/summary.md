# EMA Hourly Continuation — CVX/USDT P8_21

**Symbol:** CVX/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1652 |
| net_profit_factor | 0.4073 |
| net_win_rate | 0.4298 |
| gross_profit_factor | 0.8404 |
| gross_win_rate | 0.4504 |
| sharpe_ratio | -10.7251 |
| sortino_ratio | -6.1250 |
| max_drawdown | 0.9995 |
| cagr | -0.9522 |
| net_avg_win | 9.6748 |
| net_avg_loss | -17.9026 |
| avg_hold_time_bars | 3.3456 |
| exposure | 0.2512 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
