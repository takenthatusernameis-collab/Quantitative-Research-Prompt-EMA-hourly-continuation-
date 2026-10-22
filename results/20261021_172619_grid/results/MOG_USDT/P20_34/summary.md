# EMA Hourly Continuation — MOG/USDT P20_34

**Symbol:** MOG/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 0.7190 |
| net_win_rate | 0.4723 |
| gross_profit_factor | 0.9101 |
| gross_win_rate | 0.4723 |
| sharpe_ratio | -2.0943 |
| sortino_ratio | -0.5471 |
| max_drawdown | 0.4740 |
| cagr | -0.2222 |
| net_avg_win | 77.3976 |
| net_avg_loss | -96.3436 |
| avg_hold_time_bars | 6.0000 |
| exposure | 0.0916 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
