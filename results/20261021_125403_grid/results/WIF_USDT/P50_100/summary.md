# EMA Hourly Continuation — WIF/USDT P50_100

**Symbol:** WIF/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 338 |
| net_profit_factor | 0.8963 |
| net_win_rate | 0.5266 |
| gross_profit_factor | 1.1011 |
| gross_win_rate | 0.5266 |
| sharpe_ratio | -0.5933 |
| sortino_ratio | -0.1572 |
| max_drawdown | 0.2606 |
| cagr | -0.0729 |
| net_avg_win | 84.1459 |
| net_avg_loss | -104.4387 |
| avg_hold_time_bars | 8.9527 |
| exposure | 0.1375 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
