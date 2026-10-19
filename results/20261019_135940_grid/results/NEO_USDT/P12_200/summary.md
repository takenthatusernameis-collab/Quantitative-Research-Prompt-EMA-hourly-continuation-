# EMA Hourly Continuation — NEO/USDT P12_200

**Symbol:** NEO/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.6234 |
| net_win_rate | 0.4740 |
| gross_profit_factor | 0.9132 |
| gross_win_rate | 0.4849 |
| sharpe_ratio | -2.7209 |
| sortino_ratio | -0.7323 |
| max_drawdown | 0.5940 |
| cagr | -0.2939 |
| net_avg_win | 55.7596 |
| net_avg_loss | -80.5902 |
| avg_hold_time_bars | 45.1425 |
| exposure | 0.7490 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
