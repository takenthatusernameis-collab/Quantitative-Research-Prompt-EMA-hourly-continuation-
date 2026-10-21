# EMA Hourly Continuation — ARPA/USDT P50_89

**Symbol:** ARPA/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 420 |
| net_profit_factor | 0.5641 |
| net_win_rate | 0.4524 |
| gross_profit_factor | 0.8136 |
| gross_win_rate | 0.4548 |
| sharpe_ratio | -3.5956 |
| sortino_ratio | -1.0508 |
| max_drawdown | 0.7184 |
| cagr | -0.3821 |
| net_avg_win | 47.9008 |
| net_avg_loss | -70.1424 |
| avg_hold_time_bars | 7.5333 |
| exposure | 0.1432 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
