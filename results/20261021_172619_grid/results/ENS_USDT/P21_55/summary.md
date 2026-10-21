# EMA Hourly Continuation — ENS/USDT P21_55

**Symbol:** ENS/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 516 |
| net_profit_factor | 0.7648 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0183 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.1091 |
| sortino_ratio | -0.6872 |
| max_drawdown | 0.5698 |
| cagr | -0.2707 |
| net_avg_win | 69.0151 |
| net_avg_loss | -90.2343 |
| avg_hold_time_bars | 9.2364 |
| exposure | 0.2166 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
