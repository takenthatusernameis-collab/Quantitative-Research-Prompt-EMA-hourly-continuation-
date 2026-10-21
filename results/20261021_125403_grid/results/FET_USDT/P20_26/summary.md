# EMA Hourly Continuation — FET/USDT P20_26

**Symbol:** FET/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 139 |
| net_profit_factor | 0.7711 |
| net_win_rate | 0.5036 |
| gross_profit_factor | 1.0137 |
| gross_win_rate | 0.5036 |
| sharpe_ratio | -0.9553 |
| sortino_ratio | -0.1617 |
| max_drawdown | 0.2136 |
| cagr | -0.0714 |
| net_avg_win | 81.6387 |
| net_avg_loss | -107.4109 |
| avg_hold_time_bars | 4.9640 |
| exposure | 0.0314 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
