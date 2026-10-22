# EMA Hourly Continuation — RPL/USDT P26_144

**Symbol:** RPL/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.8823 |
| net_win_rate | 0.5152 |
| gross_profit_factor | 1.0636 |
| gross_win_rate | 0.5152 |
| sharpe_ratio | -0.7669 |
| sortino_ratio | -0.2188 |
| max_drawdown | 0.3211 |
| cagr | -0.0987 |
| net_avg_win | 84.7600 |
| net_avg_loss | -102.0704 |
| avg_hold_time_bars | 27.7424 |
| exposure | 0.4972 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
