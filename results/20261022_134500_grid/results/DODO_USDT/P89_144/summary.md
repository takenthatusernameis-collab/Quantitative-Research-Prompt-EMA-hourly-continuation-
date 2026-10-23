# EMA Hourly Continuation — DODO/USDT P89_144

**Symbol:** DODO/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 594 |
| net_profit_factor | 0.4193 |
| net_win_rate | 0.4209 |
| gross_profit_factor | 0.7130 |
| gross_win_rate | 0.4293 |
| sharpe_ratio | -6.1643 |
| sortino_ratio | -2.1243 |
| max_drawdown | 0.9245 |
| cagr | -0.6380 |
| net_avg_win | 26.6569 |
| net_avg_loss | -46.2033 |
| avg_hold_time_bars | 4.8906 |
| exposure | 0.1315 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
