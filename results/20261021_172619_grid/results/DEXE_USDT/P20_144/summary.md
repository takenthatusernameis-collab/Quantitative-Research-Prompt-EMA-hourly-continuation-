# EMA Hourly Continuation — DEXE/USDT P20_144

**Symbol:** DEXE/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 308 |
| net_profit_factor | 0.9166 |
| net_win_rate | 0.5260 |
| gross_profit_factor | 1.0882 |
| gross_win_rate | 0.5260 |
| sharpe_ratio | -0.3967 |
| sortino_ratio | -0.1001 |
| max_drawdown | 0.2965 |
| cagr | -0.0489 |
| net_avg_win | 80.2131 |
| net_avg_loss | -97.1032 |
| avg_hold_time_bars | 46.3896 |
| exposure | 0.6495 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
