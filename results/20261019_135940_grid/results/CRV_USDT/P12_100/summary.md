# EMA Hourly Continuation — CRV/USDT P12_100

**Symbol:** CRV/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 622 |
| net_profit_factor | 0.6461 |
| net_win_rate | 0.4743 |
| gross_profit_factor | 0.9647 |
| gross_win_rate | 0.4839 |
| sharpe_ratio | -3.7429 |
| sortino_ratio | -1.3085 |
| max_drawdown | 0.8097 |
| cagr | -0.4689 |
| net_avg_win | 49.2594 |
| net_avg_loss | -68.7797 |
| avg_hold_time_bars | 20.7556 |
| exposure | 0.5868 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
