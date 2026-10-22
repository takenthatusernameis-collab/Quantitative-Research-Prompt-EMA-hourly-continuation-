# EMA Hourly Continuation — TIA/USDT P55_100

**Symbol:** TIA/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 559 |
| net_profit_factor | 0.6632 |
| net_win_rate | 0.4973 |
| gross_profit_factor | 1.0187 |
| gross_win_rate | 0.5027 |
| sharpe_ratio | -3.2055 |
| sortino_ratio | -1.0694 |
| max_drawdown | 0.7268 |
| cagr | -0.4019 |
| net_avg_win | 51.3498 |
| net_avg_loss | -76.6007 |
| avg_hold_time_bars | 5.9141 |
| exposure | 0.1503 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
