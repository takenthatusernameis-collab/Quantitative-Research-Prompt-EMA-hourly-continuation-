# EMA Hourly Continuation — TNSR/USDT P50_200

**Symbol:** TNSR/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 313 |
| net_profit_factor | 0.7643 |
| net_win_rate | 0.4824 |
| gross_profit_factor | 0.9240 |
| gross_win_rate | 0.4824 |
| sharpe_ratio | -1.4678 |
| sortino_ratio | -0.3692 |
| max_drawdown | 0.3702 |
| cagr | -0.1567 |
| net_avg_win | 75.0566 |
| net_avg_loss | -91.5314 |
| avg_hold_time_bars | 28.8435 |
| exposure | 0.4086 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
