# EMA Hourly Continuation — VELO/USDT P89_144

**Symbol:** VELO/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 252 |
| net_profit_factor | 0.9308 |
| net_win_rate | 0.5397 |
| gross_profit_factor | 1.1642 |
| gross_win_rate | 0.5397 |
| sharpe_ratio | -0.3133 |
| sortino_ratio | -0.0720 |
| max_drawdown | 0.2002 |
| cagr | -0.0357 |
| net_avg_win | 86.3914 |
| net_avg_loss | -108.8157 |
| avg_hold_time_bars | 8.0556 |
| exposure | 0.0923 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
