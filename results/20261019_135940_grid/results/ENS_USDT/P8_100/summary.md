# EMA Hourly Continuation — ENS/USDT P8_100

**Symbol:** ENS/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 553 |
| net_profit_factor | 0.6646 |
| net_win_rate | 0.4864 |
| gross_profit_factor | 0.9314 |
| gross_win_rate | 0.4882 |
| sharpe_ratio | -2.8732 |
| sortino_ratio | -0.9566 |
| max_drawdown | 0.6943 |
| cagr | -0.3625 |
| net_avg_win | 49.8717 |
| net_avg_loss | -71.0794 |
| avg_hold_time_bars | 28.7071 |
| exposure | 0.7216 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
