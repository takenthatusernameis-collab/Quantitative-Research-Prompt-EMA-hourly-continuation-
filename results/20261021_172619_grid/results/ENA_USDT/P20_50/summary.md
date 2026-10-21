# EMA Hourly Continuation — ENA/USDT P20_50

**Symbol:** ENA/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 499 |
| net_profit_factor | 0.8621 |
| net_win_rate | 0.5150 |
| gross_profit_factor | 1.0490 |
| gross_win_rate | 0.5150 |
| sharpe_ratio | -0.9763 |
| sortino_ratio | -0.3136 |
| max_drawdown | 0.4252 |
| cagr | -0.1373 |
| net_avg_win | 75.3588 |
| net_avg_loss | -92.8354 |
| avg_hold_time_bars | 7.8577 |
| exposure | 0.1782 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
