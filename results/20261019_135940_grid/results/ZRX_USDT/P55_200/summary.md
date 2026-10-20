# EMA Hourly Continuation — ZRX/USDT P55_200

**Symbol:** ZRX/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.6508 |
| net_win_rate | 0.4943 |
| gross_profit_factor | 0.9549 |
| gross_win_rate | 0.4966 |
| sharpe_ratio | -2.6619 |
| sortino_ratio | -0.7792 |
| max_drawdown | 0.6170 |
| cagr | -0.3145 |
| net_avg_win | 53.1165 |
| net_avg_loss | -79.7576 |
| avg_hold_time_bars | 17.3195 |
| exposure | 0.3425 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
