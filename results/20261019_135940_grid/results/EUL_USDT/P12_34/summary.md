# EMA Hourly Continuation — EUL/USDT P12_34

**Symbol:** EUL/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1233 |
| net_profit_factor | 0.3430 |
| net_win_rate | 0.4266 |
| gross_profit_factor | 0.6140 |
| gross_win_rate | 0.4347 |
| sharpe_ratio | -8.8994 |
| sortino_ratio | -4.3918 |
| max_drawdown | 0.9958 |
| cagr | -0.8853 |
| net_avg_win | 9.8835 |
| net_avg_loss | -21.4360 |
| avg_hold_time_bars | 4.7713 |
| exposure | 0.2674 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
