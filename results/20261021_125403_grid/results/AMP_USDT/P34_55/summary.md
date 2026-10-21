# EMA Hourly Continuation — AMP/USDT P34_55

**Symbol:** AMP/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.4062 |
| net_win_rate | 0.3629 |
| gross_profit_factor | 0.5928 |
| gross_win_rate | 0.3629 |
| sharpe_ratio | -5.6237 |
| sortino_ratio | -1.5680 |
| max_drawdown | 0.8436 |
| cagr | -0.5171 |
| net_avg_win | 41.2957 |
| net_avg_loss | -57.9213 |
| avg_hold_time_bars | 5.4386 |
| exposure | 0.0947 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
