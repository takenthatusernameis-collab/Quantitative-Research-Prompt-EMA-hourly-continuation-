# EMA Hourly Continuation — STRAX/USDT P55_200

**Symbol:** STRAX/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.4913 |
| net_win_rate | 0.4099 |
| gross_profit_factor | 0.7588 |
| gross_win_rate | 0.4206 |
| sharpe_ratio | -5.1035 |
| sortino_ratio | -1.5564 |
| max_drawdown | 0.8429 |
| cagr | -0.5221 |
| net_avg_win | 42.5581 |
| net_avg_loss | -60.1667 |
| avg_hold_time_bars | 16.3455 |
| exposure | 0.3483 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
