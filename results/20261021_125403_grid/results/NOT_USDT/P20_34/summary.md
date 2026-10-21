# EMA Hourly Continuation — NOT/USDT P20_34

**Symbol:** NOT/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 261 |
| net_profit_factor | 0.8687 |
| net_win_rate | 0.5364 |
| gross_profit_factor | 1.1383 |
| gross_win_rate | 0.5364 |
| sharpe_ratio | -0.6499 |
| sortino_ratio | -0.1545 |
| max_drawdown | 0.2268 |
| cagr | -0.0701 |
| net_avg_win | 76.5581 |
| net_avg_loss | -101.9660 |
| avg_hold_time_bars | 5.3908 |
| exposure | 0.0661 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
