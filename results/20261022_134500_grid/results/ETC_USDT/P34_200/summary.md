# EMA Hourly Continuation — ETC/USDT P34_200

**Symbol:** ETC/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.6233 |
| net_win_rate | 0.4932 |
| gross_profit_factor | 1.0035 |
| gross_win_rate | 0.5014 |
| sharpe_ratio | -2.9202 |
| sortino_ratio | -0.7809 |
| max_drawdown | 0.6394 |
| cagr | -0.3176 |
| net_avg_win | 56.4018 |
| net_avg_loss | -88.0548 |
| avg_hold_time_bars | 31.3706 |
| exposure | 0.5233 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
