# EMA Hourly Continuation — WEMIX/USDT P12_21

**Symbol:** WEMIX/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 217 |
| net_profit_factor | 0.3977 |
| net_win_rate | 0.3410 |
| gross_profit_factor | 0.5488 |
| gross_win_rate | 0.3410 |
| sharpe_ratio | -4.4012 |
| sortino_ratio | -0.9146 |
| max_drawdown | 0.6665 |
| cagr | -0.3520 |
| net_avg_win | 59.2194 |
| net_avg_loss | -77.0526 |
| avg_hold_time_bars | 8.9954 |
| exposure | 0.0887 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
