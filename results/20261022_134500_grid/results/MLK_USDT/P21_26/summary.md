# EMA Hourly Continuation — MLK/USDT P21_26

**Symbol:** MLK/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1482 |
| net_profit_factor | 0.0886 |
| net_win_rate | 0.1829 |
| gross_profit_factor | 0.4175 |
| gross_win_rate | 0.2227 |
| sharpe_ratio | -23.3281 |
| sortino_ratio | -13.8133 |
| max_drawdown | 1.0000 |
| cagr | -0.9995 |
| net_avg_win | 3.5875 |
| net_avg_loss | -9.0605 |
| avg_hold_time_bars | 2.0628 |
| exposure | 0.1383 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
