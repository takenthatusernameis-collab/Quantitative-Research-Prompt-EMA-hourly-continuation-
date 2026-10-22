# EMA Hourly Continuation — NEO/USDT P12_100

**Symbol:** NEO/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 597 |
| net_profit_factor | 0.5676 |
| net_win_rate | 0.4657 |
| gross_profit_factor | 0.8877 |
| gross_win_rate | 0.4791 |
| sharpe_ratio | -4.1133 |
| sortino_ratio | -1.4165 |
| max_drawdown | 0.8183 |
| cagr | -0.4902 |
| net_avg_win | 38.5268 |
| net_avg_loss | -59.1489 |
| avg_hold_time_bars | 22.3367 |
| exposure | 0.6061 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
