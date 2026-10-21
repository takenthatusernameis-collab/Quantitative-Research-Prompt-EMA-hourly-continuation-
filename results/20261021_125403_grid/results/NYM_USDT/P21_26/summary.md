# EMA Hourly Continuation — NYM/USDT P21_26

**Symbol:** NYM/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 214 |
| net_profit_factor | 0.3154 |
| net_win_rate | 0.3972 |
| gross_profit_factor | 0.6587 |
| gross_win_rate | 0.4019 |
| sharpe_ratio | -4.5377 |
| sortino_ratio | -0.9563 |
| max_drawdown | 0.6830 |
| cagr | -0.3649 |
| net_avg_win | 36.8725 |
| net_avg_loss | -77.0260 |
| avg_hold_time_bars | 9.0514 |
| exposure | 0.0880 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
