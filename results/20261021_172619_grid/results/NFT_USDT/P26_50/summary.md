# EMA Hourly Continuation — NFT/USDT P26_50

**Symbol:** NFT/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 370 |
| net_profit_factor | 0.2539 |
| net_win_rate | 0.2459 |
| gross_profit_factor | 0.4959 |
| gross_win_rate | 0.2595 |
| sharpe_ratio | -9.2233 |
| sortino_ratio | -2.6497 |
| max_drawdown | 0.9609 |
| cagr | -0.7223 |
| net_avg_win | 35.9058 |
| net_avg_loss | -46.1176 |
| avg_hold_time_bars | 8.6676 |
| exposure | 0.1458 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
