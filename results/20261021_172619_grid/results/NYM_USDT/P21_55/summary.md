# EMA Hourly Continuation — NYM/USDT P21_55

**Symbol:** NYM/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.4973 |
| net_win_rate | 0.4409 |
| gross_profit_factor | 0.8181 |
| gross_win_rate | 0.4458 |
| sharpe_ratio | -4.1622 |
| sortino_ratio | -1.1980 |
| max_drawdown | 0.7575 |
| cagr | -0.4232 |
| net_avg_win | 41.3853 |
| net_avg_loss | -65.6259 |
| avg_hold_time_bars | 13.3768 |
| exposure | 0.2469 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
