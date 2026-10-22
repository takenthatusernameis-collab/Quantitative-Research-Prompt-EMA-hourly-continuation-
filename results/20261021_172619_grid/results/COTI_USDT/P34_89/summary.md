# EMA Hourly Continuation — COTI/USDT P34_89

**Symbol:** COTI/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 454 |
| net_profit_factor | 0.8399 |
| net_win_rate | 0.5154 |
| gross_profit_factor | 1.0593 |
| gross_win_rate | 0.5154 |
| sharpe_ratio | -1.1487 |
| sortino_ratio | -0.3520 |
| max_drawdown | 0.3771 |
| cagr | -0.1511 |
| net_avg_win | 75.5907 |
| net_avg_loss | -95.7315 |
| avg_hold_time_bars | 9.4339 |
| exposure | 0.1947 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
