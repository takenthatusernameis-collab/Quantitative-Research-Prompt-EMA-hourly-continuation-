# EMA Hourly Continuation — ONDO/USDT P55_200

**Symbol:** ONDO/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 288 |
| net_profit_factor | 0.6825 |
| net_win_rate | 0.4514 |
| gross_profit_factor | 0.8183 |
| gross_win_rate | 0.4514 |
| sharpe_ratio | -1.9845 |
| sortino_ratio | -0.4772 |
| max_drawdown | 0.4285 |
| cagr | -0.1970 |
| net_avg_win | 70.0657 |
| net_avg_loss | -84.4647 |
| avg_hold_time_bars | 23.1701 |
| exposure | 0.3033 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
