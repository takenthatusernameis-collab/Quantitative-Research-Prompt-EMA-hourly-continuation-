# EMA Hourly Continuation — ILV/USDT P21_26

**Symbol:** ILV/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1157 |
| net_profit_factor | 0.2266 |
| net_win_rate | 0.3587 |
| gross_profit_factor | 0.6986 |
| gross_win_rate | 0.4080 |
| sharpe_ratio | -14.1755 |
| sortino_ratio | -7.0179 |
| max_drawdown | 0.9999 |
| cagr | -0.9757 |
| net_avg_win | 7.0597 |
| net_avg_loss | -17.4244 |
| avg_hold_time_bars | 2.0916 |
| exposure | 0.1100 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
