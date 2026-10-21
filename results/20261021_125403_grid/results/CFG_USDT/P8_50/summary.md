# EMA Hourly Continuation — CFG/USDT P8_50

**Symbol:** CFG/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 560 |
| net_profit_factor | 0.6701 |
| net_win_rate | 0.4589 |
| gross_profit_factor | 0.8335 |
| gross_win_rate | 0.4589 |
| sharpe_ratio | -2.7590 |
| sortino_ratio | -0.9264 |
| max_drawdown | 0.6703 |
| cagr | -0.3473 |
| net_avg_win | 51.9750 |
| net_avg_loss | -65.7849 |
| avg_hold_time_bars | 20.8304 |
| exposure | 0.5302 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
