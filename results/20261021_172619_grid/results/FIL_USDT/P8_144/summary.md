# EMA Hourly Continuation — FIL/USDT P8_144

**Symbol:** FIL/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 270 |
| net_profit_factor | 0.8273 |
| net_win_rate | 0.4963 |
| gross_profit_factor | 0.9814 |
| gross_win_rate | 0.4963 |
| sharpe_ratio | -0.9736 |
| sortino_ratio | -0.2286 |
| max_drawdown | 0.3205 |
| cagr | -0.1012 |
| net_avg_win | 84.0613 |
| net_avg_loss | -100.1128 |
| avg_hold_time_bars | 66.0815 |
| exposure | 0.8110 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
