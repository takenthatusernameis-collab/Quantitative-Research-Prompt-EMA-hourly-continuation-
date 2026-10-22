# EMA Hourly Continuation — AKT/USDT P21_55

**Symbol:** AKT/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 925 |
| net_profit_factor | 0.5462 |
| net_win_rate | 0.4605 |
| gross_profit_factor | 0.9042 |
| gross_win_rate | 0.4703 |
| sharpe_ratio | -6.0224 |
| sortino_ratio | -2.5799 |
| max_drawdown | 0.9574 |
| cagr | -0.7116 |
| net_avg_win | 27.0151 |
| net_avg_loss | -42.2207 |
| avg_hold_time_bars | 5.2054 |
| exposure | 0.2189 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
