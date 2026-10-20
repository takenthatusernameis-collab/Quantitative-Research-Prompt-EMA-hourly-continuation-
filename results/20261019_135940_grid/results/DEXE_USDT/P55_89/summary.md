# EMA Hourly Continuation — DEXE/USDT P55_89

**Symbol:** DEXE/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 542 |
| net_profit_factor | 0.4017 |
| net_win_rate | 0.4428 |
| gross_profit_factor | 0.7171 |
| gross_win_rate | 0.4483 |
| sharpe_ratio | -5.4451 |
| sortino_ratio | -1.7864 |
| max_drawdown | 0.8938 |
| cagr | -0.5813 |
| net_avg_win | 24.8337 |
| net_avg_loss | -49.1294 |
| avg_hold_time_bars | 12.0129 |
| exposure | 0.2960 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
