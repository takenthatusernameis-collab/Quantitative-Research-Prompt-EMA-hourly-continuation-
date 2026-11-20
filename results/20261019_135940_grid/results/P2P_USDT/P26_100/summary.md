# EMA Hourly Continuation — P2P/USDT P26_100

**Symbol:** P2P/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 614 |
| net_profit_factor | 0.5443 |
| net_win_rate | 0.4137 |
| gross_profit_factor | 0.7257 |
| gross_win_rate | 0.4169 |
| sharpe_ratio | -4.6244 |
| sortino_ratio | -1.6063 |
| max_drawdown | 0.8527 |
| cagr | -0.5332 |
| net_avg_win | 40.0789 |
| net_avg_loss | -51.9548 |
| avg_hold_time_bars | 12.5277 |
| exposure | 0.3496 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
