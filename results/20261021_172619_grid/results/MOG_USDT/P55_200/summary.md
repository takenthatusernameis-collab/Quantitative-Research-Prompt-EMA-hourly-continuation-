# EMA Hourly Continuation — MOG/USDT P55_200

**Symbol:** MOG/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 266 |
| net_profit_factor | 0.8574 |
| net_win_rate | 0.5038 |
| gross_profit_factor | 1.0037 |
| gross_win_rate | 0.5038 |
| sharpe_ratio | -0.8218 |
| sortino_ratio | -0.2004 |
| max_drawdown | 0.2706 |
| cagr | -0.0899 |
| net_avg_win | 87.2276 |
| net_avg_loss | -103.2803 |
| avg_hold_time_bars | 25.5451 |
| exposure | 0.3378 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
