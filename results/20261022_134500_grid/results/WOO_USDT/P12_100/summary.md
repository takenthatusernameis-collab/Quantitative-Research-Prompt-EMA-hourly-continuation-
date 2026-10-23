# EMA Hourly Continuation — WOO/USDT P12_100

**Symbol:** WOO/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 611 |
| net_profit_factor | 0.7100 |
| net_win_rate | 0.4681 |
| gross_profit_factor | 1.0228 |
| gross_win_rate | 0.4861 |
| sharpe_ratio | -3.3043 |
| sortino_ratio | -1.1498 |
| max_drawdown | 0.7668 |
| cagr | -0.4200 |
| net_avg_win | 63.8176 |
| net_avg_loss | -79.0943 |
| avg_hold_time_bars | 21.3208 |
| exposure | 0.5921 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
