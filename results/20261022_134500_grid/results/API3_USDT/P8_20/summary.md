# EMA Hourly Continuation — API3/USDT P8_20

**Symbol:** API3/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1612 |
| net_profit_factor | 0.4184 |
| net_win_rate | 0.4243 |
| gross_profit_factor | 0.8781 |
| gross_win_rate | 0.4510 |
| sharpe_ratio | -11.6467 |
| sortino_ratio | -6.5957 |
| max_drawdown | 0.9998 |
| cagr | -0.9635 |
| net_avg_win | 10.5133 |
| net_avg_loss | -18.5223 |
| avg_hold_time_bars | 3.5211 |
| exposure | 0.2580 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
