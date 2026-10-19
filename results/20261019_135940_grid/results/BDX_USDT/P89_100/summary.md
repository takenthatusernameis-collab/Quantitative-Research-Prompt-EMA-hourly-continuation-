# EMA Hourly Continuation — BDX/USDT P89_100

**Symbol:** BDX/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1061 |
| net_profit_factor | 0.0805 |
| net_win_rate | 0.1668 |
| gross_profit_factor | 0.3368 |
| gross_win_rate | 0.2771 |
| sharpe_ratio | -21.4563 |
| sortino_ratio | -12.0482 |
| max_drawdown | 1.0000 |
| cagr | -0.9987 |
| net_avg_win | 4.9448 |
| net_avg_loss | -12.3023 |
| avg_hold_time_bars | 1.9067 |
| exposure | 0.0920 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
