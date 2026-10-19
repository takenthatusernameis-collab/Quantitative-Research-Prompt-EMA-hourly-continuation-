# EMA Hourly Continuation — FET/USDT P20_100

**Symbol:** FET/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 579 |
| net_profit_factor | 0.6640 |
| net_win_rate | 0.4836 |
| gross_profit_factor | 0.9402 |
| gross_win_rate | 0.4922 |
| sharpe_ratio | -2.9124 |
| sortino_ratio | -0.9879 |
| max_drawdown | 0.7038 |
| cagr | -0.3740 |
| net_avg_win | 48.8114 |
| net_avg_loss | -68.8404 |
| avg_hold_time_bars | 17.4542 |
| exposure | 0.4594 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
