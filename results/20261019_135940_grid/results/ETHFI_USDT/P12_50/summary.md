# EMA Hourly Continuation — ETHFI/USDT P12_50

**Symbol:** ETHFI/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1093 |
| net_profit_factor | 0.5292 |
| net_win_rate | 0.4346 |
| gross_profit_factor | 0.8311 |
| gross_win_rate | 0.4428 |
| sharpe_ratio | -6.9040 |
| sortino_ratio | -3.2026 |
| max_drawdown | 0.9797 |
| cagr | -0.7876 |
| net_avg_win | 23.1830 |
| net_avg_loss | -33.6693 |
| avg_hold_time_bars | 7.3092 |
| exposure | 0.3631 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
