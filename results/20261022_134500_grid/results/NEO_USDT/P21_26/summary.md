# EMA Hourly Continuation — NEO/USDT P21_26

**Symbol:** NEO/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1226 |
| net_profit_factor | 0.1832 |
| net_win_rate | 0.3385 |
| gross_profit_factor | 0.7591 |
| gross_win_rate | 0.3989 |
| sharpe_ratio | -16.2587 |
| sortino_ratio | -8.4610 |
| max_drawdown | 1.0000 |
| cagr | -0.9900 |
| net_avg_win | 5.4035 |
| net_avg_loss | -15.0954 |
| avg_hold_time_bars | 1.8817 |
| exposure | 0.1049 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
