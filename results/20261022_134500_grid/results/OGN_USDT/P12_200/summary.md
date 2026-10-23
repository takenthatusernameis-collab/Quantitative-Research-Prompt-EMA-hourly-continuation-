# EMA Hourly Continuation — OGN/USDT P12_200

**Symbol:** OGN/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.5666 |
| net_win_rate | 0.4387 |
| gross_profit_factor | 0.7946 |
| gross_win_rate | 0.4414 |
| sharpe_ratio | -3.4402 |
| sortino_ratio | -0.9246 |
| max_drawdown | 0.6971 |
| cagr | -0.3568 |
| net_avg_win | 54.5281 |
| net_avg_loss | -75.2132 |
| avg_hold_time_bars | 44.5586 |
| exposure | 0.7400 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
