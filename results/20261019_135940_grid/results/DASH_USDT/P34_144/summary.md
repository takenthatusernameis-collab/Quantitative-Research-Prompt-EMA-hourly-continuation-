# EMA Hourly Continuation — DASH/USDT P34_144

**Symbol:** DASH/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 526 |
| net_profit_factor | 0.5570 |
| net_win_rate | 0.4810 |
| gross_profit_factor | 0.9427 |
| gross_win_rate | 0.4905 |
| sharpe_ratio | -3.6427 |
| sortino_ratio | -1.1778 |
| max_drawdown | 0.7769 |
| cagr | -0.4303 |
| net_avg_win | 37.5943 |
| net_avg_loss | -62.5545 |
| avg_hold_time_bars | 16.3688 |
| exposure | 0.3914 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
