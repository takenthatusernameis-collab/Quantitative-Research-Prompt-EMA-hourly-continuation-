# EMA Hourly Continuation — LUNC/USDT P12_20

**Symbol:** LUNC/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1588 |
| net_profit_factor | 0.2506 |
| net_win_rate | 0.3684 |
| gross_profit_factor | 0.7972 |
| gross_win_rate | 0.4037 |
| sharpe_ratio | -16.4678 |
| sortino_ratio | -9.5244 |
| max_drawdown | 1.0000 |
| cagr | -0.9934 |
| net_avg_win | 5.7153 |
| net_avg_loss | -13.3035 |
| avg_hold_time_bars | 1.9528 |
| exposure | 0.1410 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
