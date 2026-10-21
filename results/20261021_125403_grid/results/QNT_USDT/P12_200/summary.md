# EMA Hourly Continuation — QNT/USDT P12_200

**Symbol:** QNT/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.8964 |
| net_win_rate | 0.5263 |
| gross_profit_factor | 1.1056 |
| gross_win_rate | 0.5263 |
| sharpe_ratio | -0.6620 |
| sortino_ratio | -0.1907 |
| max_drawdown | 0.3511 |
| cagr | -0.0871 |
| net_avg_win | 84.2902 |
| net_avg_loss | -104.4813 |
| avg_hold_time_bars | 37.4586 |
| exposure | 0.6794 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
