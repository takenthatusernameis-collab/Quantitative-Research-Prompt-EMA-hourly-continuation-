# EMA Hourly Continuation — RIO/USDT P21_144

**Symbol:** RIO/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 416 |
| net_profit_factor | 0.8174 |
| net_win_rate | 0.4784 |
| gross_profit_factor | 0.9182 |
| gross_win_rate | 0.4784 |
| sharpe_ratio | -1.3473 |
| sortino_ratio | -0.3925 |
| max_drawdown | 0.4160 |
| cagr | -0.1677 |
| net_avg_win | 82.4194 |
| net_avg_loss | -92.4704 |
| avg_hold_time_bars | 25.9615 |
| exposure | 0.4958 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
