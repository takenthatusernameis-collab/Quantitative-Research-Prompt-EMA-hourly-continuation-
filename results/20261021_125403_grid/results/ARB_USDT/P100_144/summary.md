# EMA Hourly Continuation — ARB/USDT P100_144

**Symbol:** ARB/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 209 |
| net_profit_factor | 0.8170 |
| net_win_rate | 0.5263 |
| gross_profit_factor | 1.1007 |
| gross_win_rate | 0.5263 |
| sharpe_ratio | -0.8675 |
| sortino_ratio | -0.1810 |
| max_drawdown | 0.2058 |
| cagr | -0.0803 |
| net_avg_win | 76.8902 |
| net_avg_loss | -104.5763 |
| avg_hold_time_bars | 6.5455 |
| exposure | 0.0622 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
