# EMA Hourly Continuation — VR/USDT P12_34

**Symbol:** VR/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 422 |
| net_profit_factor | 0.6542 |
| net_win_rate | 0.4739 |
| gross_profit_factor | 0.8961 |
| gross_win_rate | 0.4739 |
| sharpe_ratio | -2.7781 |
| sortino_ratio | -0.8090 |
| max_drawdown | 0.6112 |
| cagr | -0.3135 |
| net_avg_win | 57.8090 |
| net_avg_loss | -79.6113 |
| avg_hold_time_bars | 11.2938 |
| exposure | 0.2166 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
