# EMA Hourly Continuation — FLOW/USDT P8_200

**Symbol:** FLOW/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.6365 |
| net_win_rate | 0.4688 |
| gross_profit_factor | 0.8950 |
| gross_win_rate | 0.4748 |
| sharpe_ratio | -2.5071 |
| sortino_ratio | -0.6412 |
| max_drawdown | 0.5602 |
| cagr | -0.2659 |
| net_avg_win | 59.8375 |
| net_avg_loss | -82.9825 |
| avg_hold_time_bars | 53.5638 |
| exposure | 0.8205 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
