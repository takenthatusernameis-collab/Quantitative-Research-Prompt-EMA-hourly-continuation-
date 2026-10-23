# EMA Hourly Continuation — ETN/USDT P34_89

**Symbol:** ETN/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 695 |
| net_profit_factor | 0.3500 |
| net_win_rate | 0.3597 |
| gross_profit_factor | 0.5476 |
| gross_win_rate | 0.3770 |
| sharpe_ratio | -9.1251 |
| sortino_ratio | -3.7050 |
| max_drawdown | 0.9789 |
| cagr | -0.8393 |
| net_avg_win | 21.0807 |
| net_avg_loss | -33.8328 |
| avg_hold_time_bars | 6.0029 |
| exposure | 0.2266 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
