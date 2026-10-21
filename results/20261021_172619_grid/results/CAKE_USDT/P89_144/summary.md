# EMA Hourly Continuation — CAKE/USDT P89_144

**Symbol:** CAKE/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 224 |
| net_profit_factor | 0.7093 |
| net_win_rate | 0.5045 |
| gross_profit_factor | 1.0142 |
| gross_win_rate | 0.5045 |
| sharpe_ratio | -1.5899 |
| sortino_ratio | -0.3421 |
| max_drawdown | 0.3584 |
| cagr | -0.1447 |
| net_avg_win | 70.0905 |
| net_avg_loss | -100.5968 |
| avg_hold_time_bars | 7.4107 |
| exposure | 0.0755 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
