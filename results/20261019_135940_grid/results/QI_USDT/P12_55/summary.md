# EMA Hourly Continuation — QI/USDT P12_55

**Symbol:** QI/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 899 |
| net_profit_factor | 0.5469 |
| net_win_rate | 0.4627 |
| gross_profit_factor | 0.9068 |
| gross_win_rate | 0.4705 |
| sharpe_ratio | -5.7551 |
| sortino_ratio | -2.4220 |
| max_drawdown | 0.9499 |
| cagr | -0.6889 |
| net_avg_win | 27.4889 |
| net_avg_loss | -43.2915 |
| avg_hold_time_bars | 9.5239 |
| exposure | 0.3874 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
