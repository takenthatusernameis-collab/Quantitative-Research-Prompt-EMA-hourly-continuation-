# EMA Hourly Continuation — DAG/USDT P8_200

**Symbol:** DAG/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.7940 |
| net_win_rate | 0.4795 |
| gross_profit_factor | 0.9047 |
| gross_win_rate | 0.4795 |
| sharpe_ratio | -1.2711 |
| sortino_ratio | -0.3456 |
| max_drawdown | 0.4262 |
| cagr | -0.1486 |
| net_avg_win | 73.2170 |
| net_avg_loss | -84.9321 |
| avg_hold_time_bars | 42.6192 |
| exposure | 0.7071 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
