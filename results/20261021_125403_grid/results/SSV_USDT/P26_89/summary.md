# EMA Hourly Continuation — SSV/USDT P26_89

**Symbol:** SSV/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 496 |
| net_profit_factor | 0.7940 |
| net_win_rate | 0.4980 |
| gross_profit_factor | 0.9961 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.6472 |
| sortino_ratio | -0.5240 |
| max_drawdown | 0.4952 |
| cagr | -0.2151 |
| net_avg_win | 71.3624 |
| net_avg_loss | -89.1514 |
| avg_hold_time_bars | 13.7056 |
| exposure | 0.3076 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
