# EMA Hourly Continuation — LINK/USDT P8_144

**Symbol:** LINK/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 364 |
| net_profit_factor | 0.8955 |
| net_win_rate | 0.5220 |
| gross_profit_factor | 1.0872 |
| gross_win_rate | 0.5220 |
| sharpe_ratio | -0.6354 |
| sortino_ratio | -0.1745 |
| max_drawdown | 0.3074 |
| cagr | -0.0805 |
| net_avg_win | 85.6405 |
| net_avg_loss | -104.4323 |
| avg_hold_time_bars | 43.1758 |
| exposure | 0.7144 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
