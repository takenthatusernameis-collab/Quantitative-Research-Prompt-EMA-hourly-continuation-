# EMA Hourly Continuation — IOST/USDT P12_34

**Symbol:** IOST/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 713 |
| net_profit_factor | 0.6999 |
| net_win_rate | 0.4951 |
| gross_profit_factor | 1.0271 |
| gross_win_rate | 0.4965 |
| sharpe_ratio | -3.4338 |
| sortino_ratio | -1.3169 |
| max_drawdown | 0.7846 |
| cagr | -0.4532 |
| net_avg_win | 51.5737 |
| net_avg_loss | -72.2502 |
| avg_hold_time_bars | 7.6620 |
| exposure | 0.2483 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
