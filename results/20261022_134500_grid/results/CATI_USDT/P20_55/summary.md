# EMA Hourly Continuation — CATI/USDT P20_55

**Symbol:** CATI/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 866 |
| net_profit_factor | 0.4634 |
| net_win_rate | 0.4030 |
| gross_profit_factor | 0.7586 |
| gross_win_rate | 0.4296 |
| sharpe_ratio | -8.9038 |
| sortino_ratio | -4.0535 |
| max_drawdown | 0.9851 |
| cagr | -0.8648 |
| net_avg_win | 24.3568 |
| net_avg_loss | -35.4847 |
| avg_hold_time_bars | 5.8568 |
| exposure | 0.2780 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
