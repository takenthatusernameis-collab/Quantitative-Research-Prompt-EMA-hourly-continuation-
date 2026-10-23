# EMA Hourly Continuation — AUCTION/USDT P34_144

**Symbol:** AUCTION/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 569 |
| net_profit_factor | 0.6095 |
| net_win_rate | 0.4587 |
| gross_profit_factor | 0.9411 |
| gross_win_rate | 0.4728 |
| sharpe_ratio | -4.4197 |
| sortino_ratio | -1.4711 |
| max_drawdown | 0.8443 |
| cagr | -0.5137 |
| net_avg_win | 50.0963 |
| net_avg_loss | -69.6485 |
| avg_hold_time_bars | 14.7311 |
| exposure | 0.3794 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
