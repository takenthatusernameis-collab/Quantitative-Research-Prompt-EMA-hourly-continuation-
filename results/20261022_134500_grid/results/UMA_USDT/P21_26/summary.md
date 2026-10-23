# EMA Hourly Continuation — UMA/USDT P21_26

**Symbol:** UMA/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1150 |
| net_profit_factor | 0.1893 |
| net_win_rate | 0.3322 |
| gross_profit_factor | 0.6216 |
| gross_win_rate | 0.3887 |
| sharpe_ratio | -14.7630 |
| sortino_ratio | -7.3225 |
| max_drawdown | 0.9999 |
| cagr | -0.9793 |
| net_avg_win | 6.1139 |
| net_avg_loss | -16.0611 |
| avg_hold_time_bars | 2.5817 |
| exposure | 0.1350 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
