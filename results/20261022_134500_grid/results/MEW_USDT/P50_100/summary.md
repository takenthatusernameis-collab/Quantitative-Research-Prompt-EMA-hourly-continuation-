# EMA Hourly Continuation — MEW/USDT P50_100

**Symbol:** MEW/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 632 |
| net_profit_factor | 0.5579 |
| net_win_rate | 0.4509 |
| gross_profit_factor | 0.8481 |
| gross_win_rate | 0.4636 |
| sharpe_ratio | -4.7546 |
| sortino_ratio | -1.6926 |
| max_drawdown | 0.8697 |
| cagr | -0.5500 |
| net_avg_win | 38.3182 |
| net_avg_loss | -56.4110 |
| avg_hold_time_bars | 6.1930 |
| exposure | 0.1779 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
