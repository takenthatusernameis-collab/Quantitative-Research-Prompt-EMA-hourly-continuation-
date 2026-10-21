# EMA Hourly Continuation — DASH/USDT P12_144

**Symbol:** DASH/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 341 |
| net_profit_factor | 0.7547 |
| net_win_rate | 0.4839 |
| gross_profit_factor | 0.9354 |
| gross_win_rate | 0.4839 |
| sharpe_ratio | -1.5816 |
| sortino_ratio | -0.4165 |
| max_drawdown | 0.4411 |
| cagr | -0.1753 |
| net_avg_win | 71.5461 |
| net_avg_loss | -88.8770 |
| avg_hold_time_bars | 43.0088 |
| exposure | 0.6666 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
