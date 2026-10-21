# EMA Hourly Continuation — FIL/USDT P34_144

**Symbol:** FIL/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.7774 |
| net_win_rate | 0.4944 |
| gross_profit_factor | 0.9773 |
| gross_win_rate | 0.4944 |
| sharpe_ratio | -1.5047 |
| sortino_ratio | -0.4049 |
| max_drawdown | 0.4012 |
| cagr | -0.1704 |
| net_avg_win | 74.7374 |
| net_avg_loss | -93.9910 |
| avg_hold_time_bars | 22.0706 |
| exposure | 0.3551 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
