# EMA Hourly Continuation — CGPT/USDT P20_144

**Symbol:** CGPT/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 475 |
| net_profit_factor | 0.6563 |
| net_win_rate | 0.4716 |
| gross_profit_factor | 0.9428 |
| gross_win_rate | 0.4821 |
| sharpe_ratio | -3.1429 |
| sortino_ratio | -0.9524 |
| max_drawdown | 0.6976 |
| cagr | -0.3753 |
| net_avg_win | 59.0955 |
| net_avg_loss | -80.3560 |
| avg_hold_time_bars | 24.8800 |
| exposure | 0.5372 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
