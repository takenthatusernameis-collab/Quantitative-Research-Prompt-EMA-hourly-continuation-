# EMA Hourly Continuation — BRETT/USDT P12_21

**Symbol:** BRETT/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 302 |
| net_profit_factor | 0.8109 |
| net_win_rate | 0.5099 |
| gross_profit_factor | 1.0339 |
| gross_win_rate | 0.5099 |
| sharpe_ratio | -1.1589 |
| sortino_ratio | -0.2977 |
| max_drawdown | 0.3389 |
| cagr | -0.1286 |
| net_avg_win | 77.5538 |
| net_avg_loss | -99.5185 |
| avg_hold_time_bars | 5.4338 |
| exposure | 0.0790 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
