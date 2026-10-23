# EMA Hourly Continuation — ARPA/USDT P34_144

**Symbol:** ARPA/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 561 |
| net_profit_factor | 0.5419 |
| net_win_rate | 0.4403 |
| gross_profit_factor | 0.8233 |
| gross_win_rate | 0.4492 |
| sharpe_ratio | -4.7178 |
| sortino_ratio | -1.5649 |
| max_drawdown | 0.8522 |
| cagr | -0.5282 |
| net_avg_win | 40.6949 |
| net_avg_loss | -59.0721 |
| avg_hold_time_bars | 15.9608 |
| exposure | 0.4052 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
