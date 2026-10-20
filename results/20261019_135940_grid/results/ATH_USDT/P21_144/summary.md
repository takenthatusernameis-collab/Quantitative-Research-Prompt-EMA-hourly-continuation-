# EMA Hourly Continuation — ATH/USDT P21_144

**Symbol:** ATH/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.7881 |
| net_win_rate | 0.5180 |
| gross_profit_factor | 1.0927 |
| gross_win_rate | 0.5220 |
| sharpe_ratio | -1.8716 |
| sortino_ratio | -0.6125 |
| max_drawdown | 0.5120 |
| cagr | -0.2527 |
| net_avg_win | 71.2555 |
| net_avg_loss | -97.1733 |
| avg_hold_time_bars | 20.8560 |
| exposure | 0.5055 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
