# EMA Hourly Continuation — ARB/USDT P12_26

**Symbol:** ARB/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.7385 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0038 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.8557 |
| sortino_ratio | -0.5195 |
| max_drawdown | 0.4700 |
| cagr | -0.2114 |
| net_avg_win | 66.7729 |
| net_avg_loss | -90.4141 |
| avg_hold_time_bars | 5.7474 |
| exposure | 0.0993 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
