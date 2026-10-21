# EMA Hourly Continuation — UMA/USDT P12_55

**Symbol:** UMA/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 706 |
| net_profit_factor | 0.6403 |
| net_win_rate | 0.4674 |
| gross_profit_factor | 0.8560 |
| gross_win_rate | 0.4688 |
| sharpe_ratio | -3.6775 |
| sortino_ratio | -1.3916 |
| max_drawdown | 0.8063 |
| cagr | -0.4723 |
| net_avg_win | 43.1025 |
| net_avg_loss | -59.0848 |
| avg_hold_time_bars | 10.6062 |
| exposure | 0.3404 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
