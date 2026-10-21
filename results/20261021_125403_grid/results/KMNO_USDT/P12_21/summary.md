# EMA Hourly Continuation — KMNO/USDT P12_21

**Symbol:** KMNO/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.7535 |
| net_win_rate | 0.5289 |
| gross_profit_factor | 1.0994 |
| gross_win_rate | 0.5289 |
| sharpe_ratio | -1.6434 |
| sortino_ratio | -0.4645 |
| max_drawdown | 0.4372 |
| cagr | -0.1929 |
| net_avg_win | 62.5391 |
| net_avg_loss | -93.1993 |
| avg_hold_time_bars | 4.8684 |
| exposure | 0.0854 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
