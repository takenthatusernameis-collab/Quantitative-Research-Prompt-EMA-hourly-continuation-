# EMA Hourly Continuation — LUNC/USDT P21_144

**Symbol:** LUNC/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.8091 |
| net_win_rate | 0.5093 |
| gross_profit_factor | 1.0233 |
| gross_win_rate | 0.5093 |
| sharpe_ratio | -1.3209 |
| sortino_ratio | -0.3917 |
| max_drawdown | 0.4274 |
| cagr | -0.1659 |
| net_avg_win | 71.1650 |
| net_avg_loss | -91.3036 |
| avg_hold_time_bars | 23.7780 |
| exposure | 0.4626 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
