# EMA Hourly Continuation — ARB/USDT P21_55

**Symbol:** ARB/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 463 |
| net_profit_factor | 0.8434 |
| net_win_rate | 0.5270 |
| gross_profit_factor | 1.0945 |
| gross_win_rate | 0.5270 |
| sharpe_ratio | -1.0328 |
| sortino_ratio | -0.3207 |
| max_drawdown | 0.4013 |
| cagr | -0.1392 |
| net_avg_win | 69.1990 |
| net_avg_loss | -91.4182 |
| avg_hold_time_bars | 8.6652 |
| exposure | 0.1824 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
