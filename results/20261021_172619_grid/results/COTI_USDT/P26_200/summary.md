# EMA Hourly Continuation — COTI/USDT P26_200

**Symbol:** COTI/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 315 |
| net_profit_factor | 0.9685 |
| net_win_rate | 0.5333 |
| gross_profit_factor | 1.1322 |
| gross_win_rate | 0.5333 |
| sharpe_ratio | -0.1213 |
| sortino_ratio | -0.0311 |
| max_drawdown | 0.2313 |
| cagr | -0.0196 |
| net_avg_win | 88.9735 |
| net_avg_loss | -104.9880 |
| avg_hold_time_bars | 38.9460 |
| exposure | 0.5576 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
