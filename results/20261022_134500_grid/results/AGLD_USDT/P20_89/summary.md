# EMA Hourly Continuation — AGLD/USDT P20_89

**Symbol:** AGLD/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 699 |
| net_profit_factor | 0.6566 |
| net_win_rate | 0.4635 |
| gross_profit_factor | 0.9330 |
| gross_win_rate | 0.4692 |
| sharpe_ratio | -4.1052 |
| sortino_ratio | -1.5277 |
| max_drawdown | 0.8462 |
| cagr | -0.5134 |
| net_avg_win | 49.4164 |
| net_avg_loss | -65.0291 |
| avg_hold_time_bars | 13.1702 |
| exposure | 0.4166 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
