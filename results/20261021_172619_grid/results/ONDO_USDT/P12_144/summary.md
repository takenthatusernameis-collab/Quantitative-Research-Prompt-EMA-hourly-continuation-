# EMA Hourly Continuation — ONDO/USDT P12_144

**Symbol:** ONDO/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.9556 |
| net_win_rate | 0.5266 |
| gross_profit_factor | 1.1093 |
| gross_win_rate | 0.5266 |
| sharpe_ratio | -0.2382 |
| sortino_ratio | -0.0666 |
| max_drawdown | 0.2809 |
| cagr | -0.0359 |
| net_avg_win | 95.1795 |
| net_avg_loss | -110.7959 |
| avg_hold_time_bars | 35.5665 |
| exposure | 0.6079 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
