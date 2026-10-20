# EMA Hourly Continuation — COTI/USDT P12_200

**Symbol:** COTI/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 426 |
| net_profit_factor | 0.7908 |
| net_win_rate | 0.5023 |
| gross_profit_factor | 1.0458 |
| gross_win_rate | 0.5094 |
| sharpe_ratio | -1.6009 |
| sortino_ratio | -0.4674 |
| max_drawdown | 0.4944 |
| cagr | -0.1990 |
| net_avg_win | 75.4610 |
| net_avg_loss | -96.3225 |
| avg_hold_time_bars | 37.7136 |
| exposure | 0.7303 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
