# EMA Hourly Continuation — LUNA/USDT P20_200

**Symbol:** LUNA/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 338 |
| net_profit_factor | 0.8139 |
| net_win_rate | 0.4970 |
| gross_profit_factor | 0.9847 |
| gross_win_rate | 0.4970 |
| sharpe_ratio | -1.1759 |
| sortino_ratio | -0.3091 |
| max_drawdown | 0.3306 |
| cagr | -0.1342 |
| net_avg_win | 79.0372 |
| net_avg_loss | -95.9706 |
| avg_hold_time_bars | 37.8905 |
| exposure | 0.5821 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
