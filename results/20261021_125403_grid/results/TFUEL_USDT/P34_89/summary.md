# EMA Hourly Continuation — TFUEL/USDT P34_89

**Symbol:** TFUEL/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 494 |
| net_profit_factor | 0.5076 |
| net_win_rate | 0.3927 |
| gross_profit_factor | 0.6890 |
| gross_win_rate | 0.3927 |
| sharpe_ratio | -5.1891 |
| sortino_ratio | -1.6308 |
| max_drawdown | 0.8552 |
| cagr | -0.5302 |
| net_avg_win | 45.2394 |
| net_avg_loss | -57.6298 |
| avg_hold_time_bars | 9.4008 |
| exposure | 0.2101 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
