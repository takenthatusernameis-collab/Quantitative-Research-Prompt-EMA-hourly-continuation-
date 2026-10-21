# EMA Hourly Continuation — BLUR/USDT P55_144

**Symbol:** BLUR/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.8984 |
| net_win_rate | 0.5369 |
| gross_profit_factor | 1.1516 |
| gross_win_rate | 0.5369 |
| sharpe_ratio | -0.5955 |
| sortino_ratio | -0.1610 |
| max_drawdown | 0.2934 |
| cagr | -0.0747 |
| net_avg_win | 83.2036 |
| net_avg_loss | -107.3914 |
| avg_hold_time_bars | 16.5625 |
| exposure | 0.2638 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
