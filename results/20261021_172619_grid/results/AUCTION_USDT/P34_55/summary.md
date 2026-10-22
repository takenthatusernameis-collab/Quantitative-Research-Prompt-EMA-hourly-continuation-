# EMA Hourly Continuation — AUCTION/USDT P34_55

**Symbol:** AUCTION/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.5733 |
| net_win_rate | 0.4627 |
| gross_profit_factor | 0.8767 |
| gross_win_rate | 0.4627 |
| sharpe_ratio | -4.0277 |
| sortino_ratio | -1.2276 |
| max_drawdown | 0.7666 |
| cagr | -0.4346 |
| net_avg_win | 48.5627 |
| net_avg_loss | -72.9503 |
| avg_hold_time_bars | 6.0022 |
| exposure | 0.1239 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
