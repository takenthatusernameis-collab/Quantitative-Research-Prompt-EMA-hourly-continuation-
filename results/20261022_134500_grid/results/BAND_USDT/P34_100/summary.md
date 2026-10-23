# EMA Hourly Continuation — BAND/USDT P34_100

**Symbol:** BAND/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 584 |
| net_profit_factor | 0.5767 |
| net_win_rate | 0.4675 |
| gross_profit_factor | 0.8964 |
| gross_win_rate | 0.4795 |
| sharpe_ratio | -4.2069 |
| sortino_ratio | -1.4302 |
| max_drawdown | 0.8250 |
| cagr | -0.4945 |
| net_avg_win | 40.9783 |
| net_avg_loss | -62.3729 |
| avg_hold_time_bars | 11.6747 |
| exposure | 0.3085 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
