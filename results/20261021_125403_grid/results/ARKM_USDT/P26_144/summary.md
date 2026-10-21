# EMA Hourly Continuation — ARKM/USDT P26_144

**Symbol:** ARKM/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 364 |
| net_profit_factor | 0.7914 |
| net_win_rate | 0.4835 |
| gross_profit_factor | 0.9252 |
| gross_win_rate | 0.4835 |
| sharpe_ratio | -1.3534 |
| sortino_ratio | -0.3681 |
| max_drawdown | 0.3802 |
| cagr | -0.1571 |
| net_avg_win | 75.2052 |
| net_avg_loss | -88.9680 |
| avg_hold_time_bars | 27.3049 |
| exposure | 0.4518 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
