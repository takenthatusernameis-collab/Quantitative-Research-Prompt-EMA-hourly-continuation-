# EMA Hourly Continuation — AVA/USDT P12_200

**Symbol:** AVA/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 360 |
| net_profit_factor | 0.8713 |
| net_win_rate | 0.5111 |
| gross_profit_factor | 1.0296 |
| gross_win_rate | 0.5111 |
| sharpe_ratio | -0.7149 |
| sortino_ratio | -0.1947 |
| max_drawdown | 0.3398 |
| cagr | -0.0886 |
| net_avg_win | 76.4546 |
| net_avg_loss | -91.7369 |
| avg_hold_time_bars | 40.5444 |
| exposure | 0.6635 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
