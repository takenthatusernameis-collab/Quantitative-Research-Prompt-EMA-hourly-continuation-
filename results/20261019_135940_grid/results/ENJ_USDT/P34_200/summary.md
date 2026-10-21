# EMA Hourly Continuation — ENJ/USDT P34_200

**Symbol:** ENJ/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.7334 |
| net_win_rate | 0.5194 |
| gross_profit_factor | 1.0878 |
| gross_win_rate | 0.5245 |
| sharpe_ratio | -1.8295 |
| sortino_ratio | -0.5062 |
| max_drawdown | 0.4891 |
| cagr | -0.2158 |
| net_avg_win | 62.7341 |
| net_avg_loss | -92.4413 |
| avg_hold_time_bars | 30.3488 |
| exposure | 0.5315 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
