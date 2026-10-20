# EMA Hourly Continuation — FLUX/USDT P26_55

**Symbol:** FLUX/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 909 |
| net_profit_factor | 0.4653 |
| net_win_rate | 0.4532 |
| gross_profit_factor | 0.8730 |
| gross_win_rate | 0.4675 |
| sharpe_ratio | -6.9982 |
| sortino_ratio | -2.9675 |
| max_drawdown | 0.9755 |
| cagr | -0.7691 |
| net_avg_win | 20.5925 |
| net_avg_loss | -36.6842 |
| avg_hold_time_bars | 3.9417 |
| exposure | 0.1629 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
