# EMA Hourly Continuation — COMP/USDT P12_89

**Symbol:** COMP/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.7795 |
| net_win_rate | 0.5067 |
| gross_profit_factor | 1.0031 |
| gross_win_rate | 0.5067 |
| sharpe_ratio | -1.6390 |
| sortino_ratio | -0.5352 |
| max_drawdown | 0.5052 |
| cagr | -0.2191 |
| net_avg_win | 62.1807 |
| net_avg_loss | -81.9544 |
| avg_hold_time_bars | 24.9750 |
| exposure | 0.5892 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
