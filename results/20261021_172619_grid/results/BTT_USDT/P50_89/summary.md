# EMA Hourly Continuation — BTT/USDT P50_89

**Symbol:** BTT/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.4332 |
| net_win_rate | 0.4260 |
| gross_profit_factor | 0.7715 |
| gross_win_rate | 0.4290 |
| sharpe_ratio | -4.9843 |
| sortino_ratio | -1.3105 |
| max_drawdown | 0.7897 |
| cagr | -0.4607 |
| net_avg_win | 42.7062 |
| net_avg_loss | -73.1615 |
| avg_hold_time_bars | 8.8278 |
| exposure | 0.1328 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
