# EMA Hourly Continuation — PEOPLE/USDT P21_89

**Symbol:** PEOPLE/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 619 |
| net_profit_factor | 0.6078 |
| net_win_rate | 0.4604 |
| gross_profit_factor | 0.8459 |
| gross_win_rate | 0.4669 |
| sharpe_ratio | -3.8680 |
| sortino_ratio | -1.3476 |
| max_drawdown | 0.8167 |
| cagr | -0.4747 |
| net_avg_win | 43.6577 |
| net_avg_loss | -61.2911 |
| avg_hold_time_bars | 14.8029 |
| exposure | 0.4146 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
