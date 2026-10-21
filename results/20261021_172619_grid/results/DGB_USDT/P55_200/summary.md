# EMA Hourly Continuation — DGB/USDT P55_200

**Symbol:** DGB/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.6816 |
| net_win_rate | 0.4572 |
| gross_profit_factor | 0.8374 |
| gross_win_rate | 0.4572 |
| sharpe_ratio | -2.0751 |
| sortino_ratio | -0.5137 |
| max_drawdown | 0.4728 |
| cagr | -0.2107 |
| net_avg_win | 69.0222 |
| net_avg_loss | -85.3019 |
| avg_hold_time_bars | 26.0132 |
| exposure | 0.3595 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
