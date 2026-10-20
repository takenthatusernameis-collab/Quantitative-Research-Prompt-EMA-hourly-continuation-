# EMA Hourly Continuation — ANKR/USDT P12_89

**Symbol:** ANKR/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 633 |
| net_profit_factor | 0.5984 |
| net_win_rate | 0.4581 |
| gross_profit_factor | 0.9366 |
| gross_win_rate | 0.4692 |
| sharpe_ratio | -4.6455 |
| sortino_ratio | -1.6319 |
| max_drawdown | 0.8714 |
| cagr | -0.5500 |
| net_avg_win | 44.4569 |
| net_avg_loss | -62.8181 |
| avg_hold_time_bars | 20.9953 |
| exposure | 0.6041 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
