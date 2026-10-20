# EMA Hourly Continuation — ATH/USDT P20_144

**Symbol:** ATH/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.7582 |
| net_win_rate | 0.5074 |
| gross_profit_factor | 1.0557 |
| gross_win_rate | 0.5116 |
| sharpe_ratio | -2.1652 |
| sortino_ratio | -0.6867 |
| max_drawdown | 0.5666 |
| cagr | -0.2789 |
| net_avg_win | 70.1772 |
| net_avg_loss | -95.3350 |
| avg_hold_time_bars | 23.9662 |
| exposure | 0.5495 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
