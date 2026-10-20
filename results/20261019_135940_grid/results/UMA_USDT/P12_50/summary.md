# EMA Hourly Continuation — UMA/USDT P12_50

**Symbol:** UMA/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1040 |
| net_profit_factor | 0.4900 |
| net_win_rate | 0.4442 |
| gross_profit_factor | 0.8570 |
| gross_win_rate | 0.4577 |
| sharpe_ratio | -7.1271 |
| sortino_ratio | -3.2376 |
| max_drawdown | 0.9806 |
| cagr | -0.7900 |
| net_avg_win | 20.3825 |
| net_avg_loss | -33.2493 |
| avg_hold_time_bars | 7.1202 |
| exposure | 0.3366 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
