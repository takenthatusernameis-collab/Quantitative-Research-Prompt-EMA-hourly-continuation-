# EMA Hourly Continuation — ZBCN/USDT P89_144

**Symbol:** ZBCN/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 229 |
| net_profit_factor | 0.8511 |
| net_win_rate | 0.5109 |
| gross_profit_factor | 1.0351 |
| gross_win_rate | 0.5109 |
| sharpe_ratio | -0.7279 |
| sortino_ratio | -0.1596 |
| max_drawdown | 0.2442 |
| cagr | -0.0721 |
| net_avg_win | 82.3925 |
| net_avg_loss | -101.1303 |
| avg_hold_time_bars | 7.5284 |
| exposure | 0.0798 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
