# EMA Hourly Continuation — CKB/USDT P8_100

**Symbol:** CKB/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 624 |
| net_profit_factor | 0.6537 |
| net_win_rate | 0.4776 |
| gross_profit_factor | 0.9353 |
| gross_win_rate | 0.4824 |
| sharpe_ratio | -3.5825 |
| sortino_ratio | -1.2581 |
| max_drawdown | 0.7824 |
| cagr | -0.4520 |
| net_avg_win | 49.3542 |
| net_avg_loss | -69.0184 |
| avg_hold_time_bars | 24.7019 |
| exposure | 0.7006 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
