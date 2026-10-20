# EMA Hourly Continuation — POKT/USDT P12_89

**Symbol:** POKT/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 867 |
| net_profit_factor | 0.5165 |
| net_win_rate | 0.3818 |
| gross_profit_factor | 0.7665 |
| gross_win_rate | 0.3864 |
| sharpe_ratio | -7.6329 |
| sortino_ratio | -3.1353 |
| max_drawdown | 0.9794 |
| cagr | -0.7821 |
| net_avg_win | 31.5825 |
| net_avg_loss | -37.7604 |
| avg_hold_time_bars | 14.1188 |
| exposure | 0.5539 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
