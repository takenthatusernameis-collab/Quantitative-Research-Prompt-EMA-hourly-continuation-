# EMA Hourly Continuation — INJ/USDT P21_144

**Symbol:** INJ/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 364 |
| net_profit_factor | 0.8608 |
| net_win_rate | 0.5027 |
| gross_profit_factor | 1.0094 |
| gross_win_rate | 0.5027 |
| sharpe_ratio | -0.9039 |
| sortino_ratio | -0.2470 |
| max_drawdown | 0.3017 |
| cagr | -0.1097 |
| net_avg_win | 85.4826 |
| net_avg_loss | -100.4089 |
| avg_hold_time_bars | 31.3736 |
| exposure | 0.5191 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
