# EMA Hourly Continuation — REQ/USDT P26_50

**Symbol:** REQ/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1074 |
| net_profit_factor | 0.3310 |
| net_win_rate | 0.3818 |
| gross_profit_factor | 0.7821 |
| gross_win_rate | 0.4255 |
| sharpe_ratio | -11.9493 |
| sortino_ratio | -5.6189 |
| max_drawdown | 0.9993 |
| cagr | -0.9437 |
| net_avg_win | 12.0574 |
| net_avg_loss | -22.4943 |
| avg_hold_time_bars | 4.2644 |
| exposure | 0.2082 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
