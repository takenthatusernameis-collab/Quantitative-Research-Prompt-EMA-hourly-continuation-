# EMA Hourly Continuation — AVA/USDT P20_144

**Symbol:** AVA/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 426 |
| net_profit_factor | 0.8600 |
| net_win_rate | 0.5211 |
| gross_profit_factor | 1.0616 |
| gross_win_rate | 0.5211 |
| sharpe_ratio | -0.8204 |
| sortino_ratio | -0.2437 |
| max_drawdown | 0.3878 |
| cagr | -0.1091 |
| net_avg_win | 69.7320 |
| net_avg_loss | -88.2333 |
| avg_hold_time_bars | 24.5681 |
| exposure | 0.4757 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
