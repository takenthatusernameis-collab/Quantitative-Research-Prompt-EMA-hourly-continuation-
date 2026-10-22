# EMA Hourly Continuation — ELON/USDT P100_144

**Symbol:** ELON/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 208 |
| net_profit_factor | 0.6097 |
| net_win_rate | 0.4712 |
| gross_profit_factor | 0.8569 |
| gross_win_rate | 0.4712 |
| sharpe_ratio | -2.0675 |
| sortino_ratio | -0.4268 |
| max_drawdown | 0.3917 |
| cagr | -0.1770 |
| net_avg_win | 61.6652 |
| net_avg_loss | -90.1011 |
| avg_hold_time_bars | 6.9471 |
| exposure | 0.0657 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
