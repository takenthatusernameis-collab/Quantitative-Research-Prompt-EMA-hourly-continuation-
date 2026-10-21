# EMA Hourly Continuation — TWT/USDT P89_200

**Symbol:** TWT/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 292 |
| net_profit_factor | 0.6521 |
| net_win_rate | 0.4760 |
| gross_profit_factor | 0.8885 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -2.1580 |
| sortino_ratio | -0.5269 |
| max_drawdown | 0.4764 |
| cagr | -0.2142 |
| net_avg_win | 61.2315 |
| net_avg_loss | -85.3105 |
| avg_hold_time_bars | 14.1062 |
| exposure | 0.1872 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
