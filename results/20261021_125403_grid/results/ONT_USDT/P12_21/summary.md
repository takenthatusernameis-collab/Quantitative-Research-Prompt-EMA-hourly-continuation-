# EMA Hourly Continuation — ONT/USDT P12_21

**Symbol:** ONT/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.6184 |
| net_win_rate | 0.4896 |
| gross_profit_factor | 0.9432 |
| gross_win_rate | 0.4922 |
| sharpe_ratio | -2.8171 |
| sortino_ratio | -0.7921 |
| max_drawdown | 0.6187 |
| cagr | -0.3033 |
| net_avg_win | 51.5447 |
| net_avg_loss | -79.9560 |
| avg_hold_time_bars | 4.6719 |
| exposure | 0.0812 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
