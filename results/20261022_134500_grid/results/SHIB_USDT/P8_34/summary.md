# EMA Hourly Continuation — SHIB/USDT P8_34

**Symbol:** SHIB/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1443 |
| net_profit_factor | 0.4230 |
| net_win_rate | 0.4456 |
| gross_profit_factor | 0.8492 |
| gross_win_rate | 0.4643 |
| sharpe_ratio | -10.2380 |
| sortino_ratio | -5.4517 |
| max_drawdown | 0.9991 |
| cagr | -0.9374 |
| net_avg_win | 11.3907 |
| net_avg_loss | -21.6434 |
| avg_hold_time_bars | 4.8614 |
| exposure | 0.3189 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
