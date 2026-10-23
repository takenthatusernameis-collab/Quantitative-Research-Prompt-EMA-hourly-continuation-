# EMA Hourly Continuation — SSV/USDT P50_100

**Symbol:** SSV/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 724 |
| net_profit_factor | 0.4906 |
| net_win_rate | 0.4448 |
| gross_profit_factor | 0.7996 |
| gross_win_rate | 0.4544 |
| sharpe_ratio | -5.8750 |
| sortino_ratio | -2.2146 |
| max_drawdown | 0.9380 |
| cagr | -0.6598 |
| net_avg_win | 27.9431 |
| net_avg_loss | -45.6193 |
| avg_hold_time_bars | 5.5580 |
| exposure | 0.1821 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
