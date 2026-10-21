# EMA Hourly Continuation — GRT/USDT P26_144

**Symbol:** GRT/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.8589 |
| net_win_rate | 0.5115 |
| gross_profit_factor | 1.0384 |
| gross_win_rate | 0.5115 |
| sharpe_ratio | -0.9012 |
| sortino_ratio | -0.2404 |
| max_drawdown | 0.3339 |
| cagr | -0.1073 |
| net_avg_win | 85.1082 |
| net_avg_loss | -103.7548 |
| avg_hold_time_bars | 29.5891 |
| exposure | 0.4659 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
