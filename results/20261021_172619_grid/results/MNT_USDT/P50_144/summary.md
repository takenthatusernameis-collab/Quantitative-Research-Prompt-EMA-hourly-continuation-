# EMA Hourly Continuation — MNT/USDT P50_144

**Symbol:** MNT/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 290 |
| net_profit_factor | 0.7205 |
| net_win_rate | 0.4931 |
| gross_profit_factor | 0.9720 |
| gross_win_rate | 0.4931 |
| sharpe_ratio | -1.7290 |
| sortino_ratio | -0.4211 |
| max_drawdown | 0.4198 |
| cagr | -0.1769 |
| net_avg_win | 69.6953 |
| net_avg_loss | -94.1002 |
| avg_hold_time_bars | 24.0483 |
| exposure | 0.3170 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
