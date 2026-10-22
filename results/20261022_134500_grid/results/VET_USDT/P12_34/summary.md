# EMA Hourly Continuation — VET/USDT P12_34

**Symbol:** VET/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1312 |
| net_profit_factor | 0.4772 |
| net_win_rate | 0.4398 |
| gross_profit_factor | 0.9232 |
| gross_win_rate | 0.4596 |
| sharpe_ratio | -9.6249 |
| sortino_ratio | -4.8959 |
| max_drawdown | 0.9980 |
| cagr | -0.9146 |
| net_avg_win | 15.7866 |
| net_avg_loss | -25.9702 |
| avg_hold_time_bars | 4.0343 |
| exposure | 0.2406 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
