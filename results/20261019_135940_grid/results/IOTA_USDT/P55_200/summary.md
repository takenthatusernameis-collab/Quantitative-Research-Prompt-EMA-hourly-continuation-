# EMA Hourly Continuation — IOTA/USDT P55_200

**Symbol:** IOTA/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 378 |
| net_profit_factor | 0.5985 |
| net_win_rate | 0.4524 |
| gross_profit_factor | 0.8641 |
| gross_win_rate | 0.4577 |
| sharpe_ratio | -3.2940 |
| sortino_ratio | -0.9034 |
| max_drawdown | 0.6732 |
| cagr | -0.3479 |
| net_avg_win | 57.3860 |
| net_avg_loss | -79.2090 |
| avg_hold_time_bars | 20.9894 |
| exposure | 0.3606 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
