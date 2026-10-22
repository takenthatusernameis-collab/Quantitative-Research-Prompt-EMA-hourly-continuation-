# EMA Hourly Continuation — KCS/USDT P50_144

**Symbol:** KCS/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 499 |
| net_profit_factor | 0.3222 |
| net_win_rate | 0.4148 |
| gross_profit_factor | 0.7573 |
| gross_win_rate | 0.4489 |
| sharpe_ratio | -7.2883 |
| sortino_ratio | -2.3164 |
| max_drawdown | 0.9520 |
| cagr | -0.6989 |
| net_avg_win | 21.8333 |
| net_avg_loss | -48.0429 |
| avg_hold_time_bars | 14.2124 |
| exposure | 0.3224 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
