# EMA Hourly Continuation — TWT/USDT P26_144

**Symbol:** TWT/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 541 |
| net_profit_factor | 0.5532 |
| net_win_rate | 0.4677 |
| gross_profit_factor | 0.8939 |
| gross_win_rate | 0.4769 |
| sharpe_ratio | -4.2434 |
| sortino_ratio | -1.3766 |
| max_drawdown | 0.8293 |
| cagr | -0.4920 |
| net_avg_win | 40.0001 |
| net_avg_loss | -63.5245 |
| avg_hold_time_bars | 19.0481 |
| exposure | 0.4684 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
