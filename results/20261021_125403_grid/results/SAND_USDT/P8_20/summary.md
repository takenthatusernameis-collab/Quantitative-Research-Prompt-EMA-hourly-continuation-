# EMA Hourly Continuation — SAND/USDT P8_20

**Symbol:** SAND/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.7246 |
| net_win_rate | 0.5135 |
| gross_profit_factor | 1.0382 |
| gross_win_rate | 0.5135 |
| sharpe_ratio | -2.1763 |
| sortino_ratio | -0.7151 |
| max_drawdown | 0.5596 |
| cagr | -0.2786 |
| net_avg_win | 55.1518 |
| net_avg_loss | -80.3218 |
| avg_hold_time_bars | 5.8462 |
| exposure | 0.1382 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
