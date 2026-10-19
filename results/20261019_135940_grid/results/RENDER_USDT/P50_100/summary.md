# EMA Hourly Continuation — RENDER/USDT P50_100

**Symbol:** RENDER/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 569 |
| net_profit_factor | 0.5828 |
| net_win_rate | 0.4710 |
| gross_profit_factor | 0.9223 |
| gross_win_rate | 0.4763 |
| sharpe_ratio | -4.5203 |
| sortino_ratio | -1.6339 |
| max_drawdown | 0.8286 |
| cagr | -0.5450 |
| net_avg_win | 42.6291 |
| net_avg_loss | -65.1289 |
| avg_hold_time_bars | 5.6467 |
| exposure | 0.1696 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
