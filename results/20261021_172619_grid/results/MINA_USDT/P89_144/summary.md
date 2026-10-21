# EMA Hourly Continuation — MINA/USDT P89_144

**Symbol:** MINA/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 322 |
| net_profit_factor | 0.7486 |
| net_win_rate | 0.5124 |
| gross_profit_factor | 1.0282 |
| gross_win_rate | 0.5124 |
| sharpe_ratio | -1.5324 |
| sortino_ratio | -0.3950 |
| max_drawdown | 0.3908 |
| cagr | -0.1670 |
| net_avg_win | 66.4074 |
| net_avg_loss | -93.2289 |
| avg_hold_time_bars | 7.8727 |
| exposure | 0.1152 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
