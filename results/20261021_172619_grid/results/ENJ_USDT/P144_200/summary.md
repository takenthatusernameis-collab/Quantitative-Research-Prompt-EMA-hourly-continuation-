# EMA Hourly Continuation — ENJ/USDT P144_200

**Symbol:** ENJ/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 208 |
| net_profit_factor | 0.8532 |
| net_win_rate | 0.5385 |
| gross_profit_factor | 1.1591 |
| gross_win_rate | 0.5385 |
| sharpe_ratio | -0.6888 |
| sortino_ratio | -0.1434 |
| max_drawdown | 0.2156 |
| cagr | -0.0651 |
| net_avg_win | 81.0124 |
| net_avg_loss | -110.7755 |
| avg_hold_time_bars | 7.6058 |
| exposure | 0.0716 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
