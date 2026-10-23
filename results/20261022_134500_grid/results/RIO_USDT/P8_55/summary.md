# EMA Hourly Continuation — RIO/USDT P8_55

**Symbol:** RIO/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1278 |
| net_profit_factor | 0.6195 |
| net_win_rate | 0.4288 |
| gross_profit_factor | 0.8596 |
| gross_win_rate | 0.4335 |
| sharpe_ratio | -7.1258 |
| sortino_ratio | -3.5740 |
| max_drawdown | 0.9868 |
| cagr | -0.8240 |
| net_avg_win | 29.3201 |
| net_avg_loss | -35.5265 |
| avg_hold_time_bars | 7.6150 |
| exposure | 0.4468 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
