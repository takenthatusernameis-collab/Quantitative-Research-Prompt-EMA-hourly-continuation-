# EMA Hourly Continuation — WLD/USDT P21_55

**Symbol:** WLD/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 885 |
| net_profit_factor | 0.6360 |
| net_win_rate | 0.4960 |
| gross_profit_factor | 1.0121 |
| gross_win_rate | 0.5017 |
| sharpe_ratio | -4.2550 |
| sortino_ratio | -1.7872 |
| max_drawdown | 0.8891 |
| cagr | -0.5750 |
| net_avg_win | 35.1535 |
| net_avg_loss | -54.4089 |
| avg_hold_time_bars | 6.0633 |
| exposure | 0.2439 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
