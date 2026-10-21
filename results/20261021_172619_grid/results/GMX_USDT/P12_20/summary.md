# EMA Hourly Continuation — GMX/USDT P12_20

**Symbol:** GMX/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.5832 |
| net_win_rate | 0.4671 |
| gross_profit_factor | 0.8980 |
| gross_win_rate | 0.4671 |
| sharpe_ratio | -3.9526 |
| sortino_ratio | -1.2686 |
| max_drawdown | 0.7688 |
| cagr | -0.4419 |
| net_avg_win | 45.9692 |
| net_avg_loss | -69.0824 |
| avg_hold_time_bars | 5.1856 |
| exposure | 0.1181 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
