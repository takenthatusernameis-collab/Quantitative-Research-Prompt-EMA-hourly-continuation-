# EMA Hourly Continuation — CVX/USDT P55_200

**Symbol:** CVX/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 364 |
| net_profit_factor | 0.6424 |
| net_win_rate | 0.4588 |
| gross_profit_factor | 0.8700 |
| gross_win_rate | 0.4670 |
| sharpe_ratio | -2.6425 |
| sortino_ratio | -0.7078 |
| max_drawdown | 0.5750 |
| cagr | -0.2864 |
| net_avg_win | 61.4799 |
| net_avg_loss | -81.1263 |
| avg_hold_time_bars | 20.9615 |
| exposure | 0.3468 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
