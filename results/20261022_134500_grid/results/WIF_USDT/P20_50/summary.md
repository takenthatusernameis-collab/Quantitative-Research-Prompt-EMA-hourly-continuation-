# EMA Hourly Continuation — WIF/USDT P20_50

**Symbol:** WIF/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1013 |
| net_profit_factor | 0.6349 |
| net_win_rate | 0.4689 |
| gross_profit_factor | 0.9635 |
| gross_win_rate | 0.4808 |
| sharpe_ratio | -5.6737 |
| sortino_ratio | -2.5427 |
| max_drawdown | 0.9567 |
| cagr | -0.7060 |
| net_avg_win | 34.9203 |
| net_avg_loss | -48.5592 |
| avg_hold_time_bars | 4.5874 |
| exposure | 0.2112 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
