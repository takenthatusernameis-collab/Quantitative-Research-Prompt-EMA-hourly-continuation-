# EMA Hourly Continuation — TRAC/USDT P34_55

**Symbol:** TRAC/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 318 |
| net_profit_factor | 0.6595 |
| net_win_rate | 0.4906 |
| gross_profit_factor | 0.9165 |
| gross_win_rate | 0.4906 |
| sharpe_ratio | -2.0399 |
| sortino_ratio | -0.5212 |
| max_drawdown | 0.5010 |
| cagr | -0.2110 |
| net_avg_win | 55.7053 |
| net_avg_loss | -81.3328 |
| avg_hold_time_bars | 7.9686 |
| exposure | 0.1152 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
