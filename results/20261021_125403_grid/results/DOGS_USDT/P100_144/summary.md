# EMA Hourly Continuation — DOGS/USDT P100_144

**Symbol:** DOGS/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 192 |
| net_profit_factor | 0.9552 |
| net_win_rate | 0.5521 |
| gross_profit_factor | 1.2259 |
| gross_win_rate | 0.5521 |
| sharpe_ratio | -0.1861 |
| sortino_ratio | -0.0405 |
| max_drawdown | 0.1668 |
| cagr | -0.0218 |
| net_avg_win | 93.2943 |
| net_avg_loss | -120.3836 |
| avg_hold_time_bars | 6.4792 |
| exposure | 0.0660 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
