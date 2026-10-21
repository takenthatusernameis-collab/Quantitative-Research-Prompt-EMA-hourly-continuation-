# EMA Hourly Continuation — AKT/USDT P55_100

**Symbol:** AKT/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 328 |
| net_profit_factor | 0.8930 |
| net_win_rate | 0.5335 |
| gross_profit_factor | 1.1374 |
| gross_win_rate | 0.5335 |
| sharpe_ratio | -0.6096 |
| sortino_ratio | -0.1596 |
| max_drawdown | 0.2283 |
| cagr | -0.0734 |
| net_avg_win | 83.1272 |
| net_avg_loss | -106.4746 |
| avg_hold_time_bars | 8.3262 |
| exposure | 0.1241 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
