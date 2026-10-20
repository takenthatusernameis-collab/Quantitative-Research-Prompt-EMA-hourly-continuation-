# EMA Hourly Continuation — YFI/USDT P50_144

**Symbol:** YFI/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 553 |
| net_profit_factor | 0.5289 |
| net_win_rate | 0.4611 |
| gross_profit_factor | 0.9676 |
| gross_win_rate | 0.4828 |
| sharpe_ratio | -4.8016 |
| sortino_ratio | -1.5918 |
| max_drawdown | 0.8648 |
| cagr | -0.5334 |
| net_avg_win | 37.5892 |
| net_avg_loss | -60.8157 |
| avg_hold_time_bars | 12.1103 |
| exposure | 0.3030 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
