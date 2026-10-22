# EMA Hourly Continuation — JUP/USDT P26_55

**Symbol:** JUP/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 889 |
| net_profit_factor | 0.5469 |
| net_win_rate | 0.4713 |
| gross_profit_factor | 0.9393 |
| gross_win_rate | 0.4826 |
| sharpe_ratio | -5.6497 |
| sortino_ratio | -2.3766 |
| max_drawdown | 0.9458 |
| cagr | -0.6826 |
| net_avg_win | 27.1926 |
| net_avg_loss | -44.3262 |
| avg_hold_time_bars | 4.3195 |
| exposure | 0.1745 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
