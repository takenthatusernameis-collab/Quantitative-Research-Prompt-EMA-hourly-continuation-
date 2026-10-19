# EMA Hourly Continuation — DCR/USDT P21_200

**Symbol:** DCR/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 494 |
| net_profit_factor | 0.7359 |
| net_win_rate | 0.5081 |
| gross_profit_factor | 1.0605 |
| gross_win_rate | 0.5162 |
| sharpe_ratio | -2.1056 |
| sortino_ratio | -0.6654 |
| max_drawdown | 0.5938 |
| cagr | -0.2666 |
| net_avg_win | 60.2288 |
| net_avg_loss | -84.5390 |
| avg_hold_time_bars | 25.4615 |
| exposure | 0.5692 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
