# EMA Hourly Continuation — VR/USDT P26_89

**Symbol:** VR/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 795 |
| net_profit_factor | 0.4263 |
| net_win_rate | 0.3308 |
| gross_profit_factor | 0.6671 |
| gross_win_rate | 0.3434 |
| sharpe_ratio | -11.1740 |
| sortino_ratio | -4.3963 |
| max_drawdown | 0.9983 |
| cagr | -0.9204 |
| net_avg_win | 28.2040 |
| net_avg_loss | -32.7073 |
| avg_hold_time_bars | 8.8654 |
| exposure | 0.3204 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
