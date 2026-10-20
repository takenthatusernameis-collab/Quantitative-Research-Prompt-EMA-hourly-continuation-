# EMA Hourly Continuation — AEVO/USDT P20_89

**Symbol:** AEVO/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 686 |
| net_profit_factor | 0.6912 |
| net_win_rate | 0.4825 |
| gross_profit_factor | 0.9911 |
| gross_win_rate | 0.4854 |
| sharpe_ratio | -3.5801 |
| sortino_ratio | -1.3237 |
| max_drawdown | 0.8090 |
| cagr | -0.4639 |
| net_avg_win | 53.6046 |
| net_avg_loss | -72.3059 |
| avg_hold_time_bars | 13.3863 |
| exposure | 0.4155 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
