# EMA Hourly Continuation — BOSON/USDT P8_34

**Symbol:** BOSON/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1202 |
| net_profit_factor | 0.5346 |
| net_win_rate | 0.4293 |
| gross_profit_factor | 0.8461 |
| gross_win_rate | 0.4376 |
| sharpe_ratio | -7.6011 |
| sortino_ratio | -3.6658 |
| max_drawdown | 0.9894 |
| cagr | -0.8354 |
| net_avg_win | 22.0235 |
| net_avg_loss | -30.9861 |
| avg_hold_time_bars | 6.2795 |
| exposure | 0.3431 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
