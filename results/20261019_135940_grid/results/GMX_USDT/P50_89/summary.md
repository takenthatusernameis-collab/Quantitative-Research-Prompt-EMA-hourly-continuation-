# EMA Hourly Continuation — GMX/USDT P50_89

**Symbol:** GMX/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 691 |
| net_profit_factor | 0.4698 |
| net_win_rate | 0.4443 |
| gross_profit_factor | 0.8316 |
| gross_win_rate | 0.4515 |
| sharpe_ratio | -6.1460 |
| sortino_ratio | -2.2940 |
| max_drawdown | 0.9377 |
| cagr | -0.6659 |
| net_avg_win | 27.0245 |
| net_avg_loss | -45.9878 |
| avg_hold_time_bars | 5.1288 |
| exposure | 0.1611 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
