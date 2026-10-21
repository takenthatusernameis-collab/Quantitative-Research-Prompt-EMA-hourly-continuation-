# EMA Hourly Continuation — YFI/USDT P144_200

**Symbol:** YFI/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 267 |
| net_profit_factor | 0.5200 |
| net_win_rate | 0.4757 |
| gross_profit_factor | 0.8377 |
| gross_win_rate | 0.4757 |
| sharpe_ratio | -2.8544 |
| sortino_ratio | -0.6699 |
| max_drawdown | 0.5763 |
| cagr | -0.2629 |
| net_avg_win | 45.7892 |
| net_avg_loss | -79.8789 |
| avg_hold_time_bars | 7.3146 |
| exposure | 0.0884 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
