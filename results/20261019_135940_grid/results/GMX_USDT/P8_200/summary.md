# EMA Hourly Continuation — GMX/USDT P8_200

**Symbol:** GMX/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 475 |
| net_profit_factor | 0.7177 |
| net_win_rate | 0.4821 |
| gross_profit_factor | 0.9814 |
| gross_win_rate | 0.4905 |
| sharpe_ratio | -2.4600 |
| sortino_ratio | -0.7576 |
| max_drawdown | 0.6284 |
| cagr | -0.2998 |
| net_avg_win | 65.6630 |
| net_avg_loss | -85.1656 |
| avg_hold_time_bars | 35.1074 |
| exposure | 0.7580 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
