# EMA Hourly Continuation — BSV/USDT P8_200

**Symbol:** BSV/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 434 |
| net_profit_factor | 0.5314 |
| net_win_rate | 0.4470 |
| gross_profit_factor | 0.7853 |
| gross_win_rate | 0.4470 |
| sharpe_ratio | -3.8198 |
| sortino_ratio | -1.1135 |
| max_drawdown | 0.7406 |
| cagr | -0.4132 |
| net_avg_win | 43.1220 |
| net_avg_loss | -65.5983 |
| avg_hold_time_bars | 40.2028 |
| exposure | 0.7931 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
