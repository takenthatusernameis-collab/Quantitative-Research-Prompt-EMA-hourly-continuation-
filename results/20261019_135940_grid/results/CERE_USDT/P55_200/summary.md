# EMA Hourly Continuation — CERE/USDT P55_200

**Symbol:** CERE/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 441 |
| net_profit_factor | 0.4809 |
| net_win_rate | 0.3288 |
| gross_profit_factor | 0.7261 |
| gross_win_rate | 0.3447 |
| sharpe_ratio | -7.4731 |
| sortino_ratio | -2.2171 |
| max_drawdown | 0.9458 |
| cagr | -0.6820 |
| net_avg_win | 60.2942 |
| net_avg_loss | -61.4180 |
| avg_hold_time_bars | 18.9819 |
| exposure | 0.3805 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
