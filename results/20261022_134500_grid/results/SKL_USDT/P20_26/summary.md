# EMA Hourly Continuation — SKL/USDT P20_26

**Symbol:** SKL/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1260 |
| net_profit_factor | 0.2561 |
| net_win_rate | 0.3786 |
| gross_profit_factor | 0.7009 |
| gross_win_rate | 0.4262 |
| sharpe_ratio | -13.9223 |
| sortino_ratio | -7.1220 |
| max_drawdown | 0.9999 |
| cagr | -0.9774 |
| net_avg_win | 7.2161 |
| net_avg_loss | -17.1665 |
| avg_hold_time_bars | 1.9881 |
| exposure | 0.1139 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
