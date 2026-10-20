# EMA Hourly Continuation — POKT/USDT P8_50

**Symbol:** POKT/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1257 |
| net_profit_factor | 0.5171 |
| net_win_rate | 0.4105 |
| gross_profit_factor | 0.8528 |
| gross_win_rate | 0.4208 |
| sharpe_ratio | -8.7239 |
| sortino_ratio | -4.3238 |
| max_drawdown | 0.9951 |
| cagr | -0.8781 |
| net_avg_win | 20.6527 |
| net_avg_loss | -27.8102 |
| avg_hold_time_bars | 7.7868 |
| exposure | 0.4429 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
