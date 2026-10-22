# EMA Hourly Continuation — ETC/USDT P20_144

**Symbol:** ETC/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 545 |
| net_profit_factor | 0.5411 |
| net_win_rate | 0.4661 |
| gross_profit_factor | 0.9316 |
| gross_win_rate | 0.4789 |
| sharpe_ratio | -4.5312 |
| sortino_ratio | -1.4849 |
| max_drawdown | 0.8438 |
| cagr | -0.5146 |
| net_avg_win | 38.8699 |
| net_avg_loss | -62.6978 |
| avg_hold_time_bars | 20.2991 |
| exposure | 0.5029 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
