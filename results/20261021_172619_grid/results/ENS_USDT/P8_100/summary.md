# EMA Hourly Continuation — ENS/USDT P8_100

**Symbol:** ENS/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 416 |
| net_profit_factor | 0.8126 |
| net_win_rate | 0.4976 |
| gross_profit_factor | 0.9762 |
| gross_win_rate | 0.4976 |
| sharpe_ratio | -1.2463 |
| sortino_ratio | -0.3634 |
| max_drawdown | 0.4085 |
| cagr | -0.1558 |
| net_avg_win | 72.5798 |
| net_avg_loss | -88.4620 |
| avg_hold_time_bars | 37.5769 |
| exposure | 0.7105 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
