# EMA Hourly Continuation — XAI/USDT P55_89

**Symbol:** XAI/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 718 |
| net_profit_factor | 0.5744 |
| net_win_rate | 0.4610 |
| gross_profit_factor | 0.9389 |
| gross_win_rate | 0.4708 |
| sharpe_ratio | -5.5482 |
| sortino_ratio | -2.1010 |
| max_drawdown | 0.9244 |
| cagr | -0.6368 |
| net_avg_win | 37.5641 |
| net_avg_loss | -55.9374 |
| avg_hold_time_bars | 4.1323 |
| exposure | 0.1349 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
