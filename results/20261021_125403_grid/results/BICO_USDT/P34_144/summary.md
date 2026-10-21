# EMA Hourly Continuation — BICO/USDT P34_144

**Symbol:** BICO/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.7325 |
| net_win_rate | 0.4746 |
| gross_profit_factor | 0.8825 |
| gross_win_rate | 0.4746 |
| sharpe_ratio | -1.7140 |
| sortino_ratio | -0.4589 |
| max_drawdown | 0.4431 |
| cagr | -0.1910 |
| net_avg_win | 67.2831 |
| net_avg_loss | -82.9599 |
| avg_hold_time_bars | 28.2910 |
| exposure | 0.4552 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
