# EMA Hourly Continuation — VET/USDT P8_144

**Symbol:** VET/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.6368 |
| net_win_rate | 0.4777 |
| gross_profit_factor | 0.9616 |
| gross_win_rate | 0.4933 |
| sharpe_ratio | -3.0085 |
| sortino_ratio | -0.8877 |
| max_drawdown | 0.6860 |
| cagr | -0.3519 |
| net_avg_win | 54.3533 |
| net_avg_loss | -78.0635 |
| avg_hold_time_bars | 37.5335 |
| exposure | 0.7643 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
