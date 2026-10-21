# EMA Hourly Continuation — SUI/USDT P50_144

**Symbol:** SUI/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 326 |
| net_profit_factor | 0.8381 |
| net_win_rate | 0.5123 |
| gross_profit_factor | 1.0473 |
| gross_win_rate | 0.5123 |
| sharpe_ratio | -1.0179 |
| sortino_ratio | -0.2639 |
| max_drawdown | 0.3519 |
| cagr | -0.1158 |
| net_avg_win | 82.4045 |
| net_avg_loss | -103.2760 |
| avg_hold_time_bars | 15.6350 |
| exposure | 0.2317 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
