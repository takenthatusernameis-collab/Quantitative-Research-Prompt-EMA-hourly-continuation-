# EMA Hourly Continuation — AUCTION/USDT P26_100

**Symbol:** AUCTION/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 534 |
| net_profit_factor | 0.6654 |
| net_win_rate | 0.4719 |
| gross_profit_factor | 0.9141 |
| gross_win_rate | 0.4738 |
| sharpe_ratio | -3.2562 |
| sortino_ratio | -1.0654 |
| max_drawdown | 0.7318 |
| cagr | -0.3921 |
| net_avg_win | 56.4278 |
| net_avg_loss | -75.7817 |
| avg_hold_time_bars | 14.2753 |
| exposure | 0.3450 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
