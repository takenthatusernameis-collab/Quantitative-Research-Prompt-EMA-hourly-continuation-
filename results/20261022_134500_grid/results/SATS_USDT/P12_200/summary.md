# EMA Hourly Continuation — SATS/USDT P12_200

**Symbol:** SATS/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.6147 |
| net_win_rate | 0.4675 |
| gross_profit_factor | 0.8721 |
| gross_win_rate | 0.4723 |
| sharpe_ratio | -2.7239 |
| sortino_ratio | -0.7748 |
| max_drawdown | 0.6198 |
| cagr | -0.3084 |
| net_avg_win | 49.8047 |
| net_avg_loss | -71.1206 |
| avg_hold_time_bars | 37.9590 |
| exposure | 0.7128 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
