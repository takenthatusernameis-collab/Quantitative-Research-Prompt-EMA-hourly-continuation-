# EMA Hourly Continuation — JST/USDT P100_200

**Symbol:** JST/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 359 |
| net_profit_factor | 0.4739 |
| net_win_rate | 0.4763 |
| gross_profit_factor | 1.0430 |
| gross_win_rate | 0.5070 |
| sharpe_ratio | -4.1311 |
| sortino_ratio | -1.1090 |
| max_drawdown | 0.7592 |
| cagr | -0.4175 |
| net_avg_win | 39.1933 |
| net_avg_loss | -75.2318 |
| avg_hold_time_bars | 10.8106 |
| exposure | 0.1756 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
