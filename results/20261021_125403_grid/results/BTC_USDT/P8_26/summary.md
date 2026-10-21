# EMA Hourly Continuation — BTC/USDT P8_26

**Symbol:** BTC/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 699 |
| net_profit_factor | 0.5255 |
| net_win_rate | 0.4936 |
| gross_profit_factor | 0.9661 |
| gross_win_rate | 0.5007 |
| sharpe_ratio | -5.0432 |
| sortino_ratio | -1.8029 |
| max_drawdown | 0.9078 |
| cagr | -0.5663 |
| net_avg_win | 29.1455 |
| net_avg_loss | -54.0499 |
| avg_hold_time_bars | 7.3262 |
| exposure | 0.2048 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
