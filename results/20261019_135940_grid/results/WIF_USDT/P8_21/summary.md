# EMA Hourly Continuation — WIF/USDT P8_21

**Symbol:** WIF/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1657 |
| net_profit_factor | 0.5497 |
| net_win_rate | 0.4418 |
| gross_profit_factor | 0.9081 |
| gross_win_rate | 0.4532 |
| sharpe_ratio | -10.0075 |
| sortino_ratio | -5.7282 |
| max_drawdown | 0.9992 |
| cagr | -0.9410 |
| net_avg_win | 16.6665 |
| net_avg_loss | -23.9910 |
| avg_hold_time_bars | 2.8340 |
| exposure | 0.2135 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
