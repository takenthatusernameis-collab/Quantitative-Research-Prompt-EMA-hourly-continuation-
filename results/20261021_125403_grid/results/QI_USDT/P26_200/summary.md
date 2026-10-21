# EMA Hourly Continuation — QI/USDT P26_200

**Symbol:** QI/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.7467 |
| net_win_rate | 0.4824 |
| gross_profit_factor | 0.9305 |
| gross_win_rate | 0.4824 |
| sharpe_ratio | -1.6858 |
| sortino_ratio | -0.4422 |
| max_drawdown | 0.4304 |
| cagr | -0.1848 |
| net_avg_win | 72.3759 |
| net_avg_loss | -90.3198 |
| avg_hold_time_bars | 32.0176 |
| exposure | 0.4926 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
