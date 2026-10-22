# EMA Hourly Continuation — FET/USDT P12_34

**Symbol:** FET/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1348 |
| net_profit_factor | 0.5100 |
| net_win_rate | 0.4555 |
| gross_profit_factor | 0.8574 |
| gross_win_rate | 0.4651 |
| sharpe_ratio | -8.1093 |
| sortino_ratio | -4.1899 |
| max_drawdown | 0.9942 |
| cagr | -0.8717 |
| net_avg_win | 16.8536 |
| net_avg_loss | -27.6437 |
| avg_hold_time_bars | 3.6766 |
| exposure | 0.2253 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
