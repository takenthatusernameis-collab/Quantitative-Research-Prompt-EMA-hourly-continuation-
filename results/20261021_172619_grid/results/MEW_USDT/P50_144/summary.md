# EMA Hourly Continuation — MEW/USDT P50_144

**Symbol:** MEW/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 359 |
| net_profit_factor | 0.8363 |
| net_win_rate | 0.5070 |
| gross_profit_factor | 1.0170 |
| gross_win_rate | 0.5070 |
| sharpe_ratio | -1.0017 |
| sortino_ratio | -0.2722 |
| max_drawdown | 0.2992 |
| cagr | -0.1192 |
| net_avg_win | 76.6087 |
| net_avg_loss | -94.1931 |
| avg_hold_time_bars | 16.3538 |
| exposure | 0.2669 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
