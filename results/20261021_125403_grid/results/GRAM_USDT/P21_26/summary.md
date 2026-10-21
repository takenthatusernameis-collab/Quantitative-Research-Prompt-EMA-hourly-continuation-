# EMA Hourly Continuation — GRAM/USDT P21_26

**Symbol:** GRAM/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 108 |
| net_profit_factor | 0.5315 |
| net_win_rate | 0.4444 |
| gross_profit_factor | 0.8031 |
| gross_win_rate | 0.4444 |
| sharpe_ratio | -2.0169 |
| sortino_ratio | -0.3001 |
| max_drawdown | 0.2939 |
| cagr | -0.1294 |
| net_avg_win | 69.4488 |
| net_avg_loss | -104.5367 |
| avg_hold_time_bars | 5.3704 |
| exposure | 0.0264 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
