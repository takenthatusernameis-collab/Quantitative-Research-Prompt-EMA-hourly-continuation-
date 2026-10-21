# EMA Hourly Continuation — QNT/USDT P34_100

**Symbol:** QNT/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 503 |
| net_profit_factor | 0.7023 |
| net_win_rate | 0.4911 |
| gross_profit_factor | 0.9620 |
| gross_win_rate | 0.4911 |
| sharpe_ratio | -2.4726 |
| sortino_ratio | -0.7946 |
| max_drawdown | 0.6201 |
| cagr | -0.3040 |
| net_avg_win | 57.0578 |
| net_avg_loss | -78.3930 |
| avg_hold_time_bars | 9.6183 |
| exposure | 0.2199 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
