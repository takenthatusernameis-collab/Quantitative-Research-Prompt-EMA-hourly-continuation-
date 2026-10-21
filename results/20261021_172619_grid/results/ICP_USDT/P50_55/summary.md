# EMA Hourly Continuation — ICP/USDT P50_55

**Symbol:** ICP/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 96 |
| net_profit_factor | 0.5643 |
| net_win_rate | 0.4375 |
| gross_profit_factor | 0.7821 |
| gross_win_rate | 0.4375 |
| sharpe_ratio | -1.7468 |
| sortino_ratio | -0.2440 |
| max_drawdown | 0.2912 |
| cagr | -0.1059 |
| net_avg_win | 75.5771 |
| net_avg_loss | -104.1673 |
| avg_hold_time_bars | 5.0104 |
| exposure | 0.0219 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
