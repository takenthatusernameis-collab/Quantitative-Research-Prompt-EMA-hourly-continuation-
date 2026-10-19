# EMA Hourly Continuation — RENDER/USDT P55_200

**Symbol:** RENDER/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 330 |
| net_profit_factor | 0.7516 |
| net_win_rate | 0.5152 |
| gross_profit_factor | 1.0866 |
| gross_win_rate | 0.5212 |
| sharpe_ratio | -1.7308 |
| sortino_ratio | -0.4765 |
| max_drawdown | 0.4153 |
| cagr | -0.2059 |
| net_avg_win | 69.8859 |
| net_avg_loss | -98.7905 |
| avg_hold_time_bars | 21.1424 |
| exposure | 0.3682 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
