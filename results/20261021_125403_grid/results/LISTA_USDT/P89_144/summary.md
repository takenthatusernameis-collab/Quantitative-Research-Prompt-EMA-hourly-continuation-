# EMA Hourly Continuation — LISTA/USDT P89_144

**Symbol:** LISTA/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 298 |
| net_profit_factor | 0.7005 |
| net_win_rate | 0.4799 |
| gross_profit_factor | 0.9130 |
| gross_win_rate | 0.4799 |
| sharpe_ratio | -1.9804 |
| sortino_ratio | -0.5064 |
| max_drawdown | 0.4334 |
| cagr | -0.2074 |
| net_avg_win | 68.5076 |
| net_avg_loss | -90.2207 |
| avg_hold_time_bars | 7.8154 |
| exposure | 0.1139 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
