# EMA Hourly Continuation — NOT/USDT P34_55

**Symbol:** NOT/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.7975 |
| net_win_rate | 0.5125 |
| gross_profit_factor | 1.0417 |
| gross_win_rate | 0.5125 |
| sharpe_ratio | -1.1959 |
| sortino_ratio | -0.2931 |
| max_drawdown | 0.3320 |
| cagr | -0.1267 |
| net_avg_win | 76.6987 |
| net_avg_loss | -101.0887 |
| avg_hold_time_bars | 5.6441 |
| exposure | 0.0745 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
