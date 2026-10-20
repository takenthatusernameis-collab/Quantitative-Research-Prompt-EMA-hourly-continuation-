# EMA Hourly Continuation — UQC/USDT P26_34

**Symbol:** UQC/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 441 |
| net_profit_factor | 0.0664 |
| net_win_rate | 0.2245 |
| gross_profit_factor | 0.2467 |
| gross_win_rate | 0.2494 |
| sharpe_ratio | -11.0761 |
| sortino_ratio | -3.4555 |
| max_drawdown | 0.9931 |
| cagr | -0.8609 |
| net_avg_win | 7.1305 |
| net_avg_loss | -31.1019 |
| avg_hold_time_bars | 23.6100 |
| exposure | 0.4712 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
