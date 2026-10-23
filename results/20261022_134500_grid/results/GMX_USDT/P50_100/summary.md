# EMA Hourly Continuation — GMX/USDT P50_100

**Symbol:** GMX/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 641 |
| net_profit_factor | 0.4759 |
| net_win_rate | 0.4462 |
| gross_profit_factor | 0.8263 |
| gross_win_rate | 0.4540 |
| sharpe_ratio | -5.5994 |
| sortino_ratio | -2.0124 |
| max_drawdown | 0.9115 |
| cagr | -0.6156 |
| net_avg_win | 28.8730 |
| net_avg_loss | -48.8780 |
| avg_hold_time_bars | 6.5772 |
| exposure | 0.1916 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
