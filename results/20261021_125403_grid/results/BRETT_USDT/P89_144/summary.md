# EMA Hourly Continuation — BRETT/USDT P89_144

**Symbol:** BRETT/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 253 |
| net_profit_factor | 0.7990 |
| net_win_rate | 0.4941 |
| gross_profit_factor | 0.9764 |
| gross_win_rate | 0.4980 |
| sharpe_ratio | -1.1259 |
| sortino_ratio | -0.2635 |
| max_drawdown | 0.2847 |
| cagr | -0.1147 |
| net_avg_win | 79.8215 |
| net_avg_loss | -97.5615 |
| avg_hold_time_bars | 8.3794 |
| exposure | 0.1020 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
