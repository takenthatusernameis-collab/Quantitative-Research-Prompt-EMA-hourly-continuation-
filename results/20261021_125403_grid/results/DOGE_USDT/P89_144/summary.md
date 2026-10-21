# EMA Hourly Continuation — DOGE/USDT P89_144

**Symbol:** DOGE/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 228 |
| net_profit_factor | 0.7426 |
| net_win_rate | 0.5044 |
| gross_profit_factor | 1.0151 |
| gross_win_rate | 0.5044 |
| sharpe_ratio | -1.4144 |
| sortino_ratio | -0.3068 |
| max_drawdown | 0.3135 |
| cagr | -0.1312 |
| net_avg_win | 74.6805 |
| net_avg_loss | -102.3425 |
| avg_hold_time_bars | 8.1842 |
| exposure | 0.0848 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
