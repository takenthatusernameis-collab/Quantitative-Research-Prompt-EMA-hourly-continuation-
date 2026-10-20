# EMA Hourly Continuation — G/USDT P100_200

**Symbol:** G/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 326 |
| net_profit_factor | 0.5003 |
| net_win_rate | 0.4540 |
| gross_profit_factor | 0.8236 |
| gross_win_rate | 0.4571 |
| sharpe_ratio | -4.0032 |
| sortino_ratio | -1.0940 |
| max_drawdown | 0.6957 |
| cagr | -0.4102 |
| net_avg_win | 46.1576 |
| net_avg_loss | -76.7036 |
| avg_hold_time_bars | 10.2178 |
| exposure | 0.1751 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
