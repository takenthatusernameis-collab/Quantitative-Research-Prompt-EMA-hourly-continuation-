# EMA Hourly Continuation — CARV/USDT P20_21

**Symbol:** CARV/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 900 |
| net_profit_factor | 0.2172 |
| net_win_rate | 0.3400 |
| gross_profit_factor | 0.7449 |
| gross_win_rate | 0.4422 |
| sharpe_ratio | -15.5795 |
| sortino_ratio | -7.7796 |
| max_drawdown | 0.9998 |
| cagr | -0.9856 |
| net_avg_win | 9.0649 |
| net_avg_loss | -21.5017 |
| avg_hold_time_bars | 2.4744 |
| exposure | 0.1253 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
