# EMA Hourly Continuation — CKB/USDT P21_144

**Symbol:** CKB/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.8002 |
| net_win_rate | 0.5024 |
| gross_profit_factor | 0.9875 |
| gross_win_rate | 0.5024 |
| sharpe_ratio | -1.3331 |
| sortino_ratio | -0.3875 |
| max_drawdown | 0.3934 |
| cagr | -0.1647 |
| net_avg_win | 70.3501 |
| net_avg_loss | -88.7746 |
| avg_hold_time_bars | 26.3786 |
| exposure | 0.4940 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
