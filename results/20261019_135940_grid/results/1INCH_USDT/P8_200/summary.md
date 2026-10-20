# EMA Hourly Continuation — 1INCH/USDT P8_200

**Symbol:** 1INCH/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 0.5991 |
| net_win_rate | 0.4475 |
| gross_profit_factor | 0.8702 |
| gross_win_rate | 0.4669 |
| sharpe_ratio | -2.5266 |
| sortino_ratio | -0.5738 |
| max_drawdown | 0.4975 |
| cagr | -0.2339 |
| net_avg_win | 63.3825 |
| net_avg_loss | -85.6861 |
| avg_hold_time_bars | 73.4047 |
| exposure | 0.8575 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
