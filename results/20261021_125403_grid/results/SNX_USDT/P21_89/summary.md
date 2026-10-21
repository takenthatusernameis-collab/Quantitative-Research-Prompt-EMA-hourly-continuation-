# EMA Hourly Continuation — SNX/USDT P21_89

**Symbol:** SNX/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.9051 |
| net_win_rate | 0.5320 |
| gross_profit_factor | 1.1310 |
| gross_win_rate | 0.5320 |
| sharpe_ratio | -0.6773 |
| sortino_ratio | -0.2182 |
| max_drawdown | 0.3447 |
| cagr | -0.1001 |
| net_avg_win | 83.7359 |
| net_avg_loss | -105.1728 |
| avg_hold_time_bars | 14.5840 |
| exposure | 0.3300 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
