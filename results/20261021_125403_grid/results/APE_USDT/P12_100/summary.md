# EMA Hourly Continuation — APE/USDT P12_100

**Symbol:** APE/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.7292 |
| net_win_rate | 0.4676 |
| gross_profit_factor | 0.8901 |
| gross_win_rate | 0.4676 |
| sharpe_ratio | -2.2718 |
| sortino_ratio | -0.7071 |
| max_drawdown | 0.5695 |
| cagr | -0.2779 |
| net_avg_win | 67.1218 |
| net_avg_loss | -80.8633 |
| avg_hold_time_bars | 26.2505 |
| exposure | 0.5715 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
