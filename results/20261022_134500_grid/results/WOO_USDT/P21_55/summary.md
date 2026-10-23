# EMA Hourly Continuation — WOO/USDT P21_55

**Symbol:** WOO/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 877 |
| net_profit_factor | 0.6326 |
| net_win_rate | 0.4664 |
| gross_profit_factor | 1.0512 |
| gross_win_rate | 0.4812 |
| sharpe_ratio | -5.4877 |
| sortino_ratio | -2.2858 |
| max_drawdown | 0.9405 |
| cagr | -0.6683 |
| net_avg_win | 39.4594 |
| net_avg_loss | -54.5152 |
| avg_hold_time_bars | 6.2018 |
| exposure | 0.2472 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
