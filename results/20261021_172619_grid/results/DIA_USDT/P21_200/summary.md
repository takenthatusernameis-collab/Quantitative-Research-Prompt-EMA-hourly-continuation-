# EMA Hourly Continuation — DIA/USDT P21_200

**Symbol:** DIA/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 326 |
| net_profit_factor | 0.9699 |
| net_win_rate | 0.5429 |
| gross_profit_factor | 1.1724 |
| gross_win_rate | 0.5429 |
| sharpe_ratio | -0.1073 |
| sortino_ratio | -0.0280 |
| max_drawdown | 0.3118 |
| cagr | -0.0185 |
| net_avg_win | 83.5446 |
| net_avg_loss | -102.3244 |
| avg_hold_time_bars | 41.9877 |
| exposure | 0.6194 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
