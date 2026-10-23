# EMA Hourly Continuation — ORDI/USDT P21_144

**Symbol:** ORDI/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 531 |
| net_profit_factor | 0.6195 |
| net_win_rate | 0.4482 |
| gross_profit_factor | 0.8277 |
| gross_win_rate | 0.4501 |
| sharpe_ratio | -3.6776 |
| sortino_ratio | -1.1975 |
| max_drawdown | 0.7619 |
| cagr | -0.4298 |
| net_avg_win | 51.7156 |
| net_avg_loss | -67.8122 |
| avg_hold_time_bars | 20.5235 |
| exposure | 0.4954 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
