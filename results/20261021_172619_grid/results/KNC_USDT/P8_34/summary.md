# EMA Hourly Continuation — KNC/USDT P8_34

**Symbol:** KNC/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 857 |
| net_profit_factor | 0.6414 |
| net_win_rate | 0.4691 |
| gross_profit_factor | 0.9264 |
| gross_win_rate | 0.4714 |
| sharpe_ratio | -4.6241 |
| sortino_ratio | -1.9335 |
| max_drawdown | 0.8972 |
| cagr | -0.5887 |
| net_avg_win | 39.7216 |
| net_avg_loss | -54.7121 |
| avg_hold_time_bars | 8.9265 |
| exposure | 0.3477 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
