# EMA Hourly Continuation — BICO/USDT P26_89

**Symbol:** BICO/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 675 |
| net_profit_factor | 0.5559 |
| net_win_rate | 0.4474 |
| gross_profit_factor | 0.8188 |
| gross_win_rate | 0.4533 |
| sharpe_ratio | -4.5639 |
| sortino_ratio | -1.6687 |
| max_drawdown | 0.8730 |
| cagr | -0.5474 |
| net_avg_win | 35.7819 |
| net_avg_loss | -52.1196 |
| avg_hold_time_bars | 11.3689 |
| exposure | 0.3488 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
