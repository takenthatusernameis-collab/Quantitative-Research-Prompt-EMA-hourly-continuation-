# EMA Hourly Continuation — NEO/USDT P8_200

**Symbol:** NEO/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.6798 |
| net_win_rate | 0.4926 |
| gross_profit_factor | 1.0057 |
| gross_win_rate | 0.5015 |
| sharpe_ratio | -2.1478 |
| sortino_ratio | -0.5546 |
| max_drawdown | 0.5626 |
| cagr | -0.2339 |
| net_avg_win | 62.0205 |
| net_avg_loss | -88.5786 |
| avg_hold_time_bars | 53.4956 |
| exposure | 0.8243 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
