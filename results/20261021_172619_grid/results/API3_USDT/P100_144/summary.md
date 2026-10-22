# EMA Hourly Continuation — API3/USDT P100_144

**Symbol:** API3/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 262 |
| net_profit_factor | 0.7565 |
| net_win_rate | 0.5153 |
| gross_profit_factor | 1.0376 |
| gross_win_rate | 0.5153 |
| sharpe_ratio | -1.3200 |
| sortino_ratio | -0.3076 |
| max_drawdown | 0.3439 |
| cagr | -0.1316 |
| net_avg_win | 68.6726 |
| net_avg_loss | -96.4969 |
| avg_hold_time_bars | 6.0000 |
| exposure | 0.0715 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
