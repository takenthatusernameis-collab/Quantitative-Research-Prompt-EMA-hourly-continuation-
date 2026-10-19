# EMA Hourly Continuation — SHIB/USDT P55_144

**Symbol:** SHIB/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 498 |
| net_profit_factor | 0.5216 |
| net_win_rate | 0.4618 |
| gross_profit_factor | 0.8906 |
| gross_win_rate | 0.4719 |
| sharpe_ratio | -4.5091 |
| sortino_ratio | -1.4081 |
| max_drawdown | 0.8299 |
| cagr | -0.4986 |
| net_avg_win | 39.0321 |
| net_avg_loss | -64.2196 |
| avg_hold_time_bars | 10.7992 |
| exposure | 0.2445 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
