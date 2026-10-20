# EMA Hourly Continuation — GMX/USDT P50_55

**Symbol:** GMX/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 838 |
| net_profit_factor | 0.2069 |
| net_win_rate | 0.3353 |
| gross_profit_factor | 0.6817 |
| gross_win_rate | 0.4010 |
| sharpe_ratio | -12.5948 |
| sortino_ratio | -5.3439 |
| max_drawdown | 0.9992 |
| cagr | -0.9412 |
| net_avg_win | 9.2781 |
| net_avg_loss | -22.6195 |
| avg_hold_time_bars | 2.5728 |
| exposure | 0.0980 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
