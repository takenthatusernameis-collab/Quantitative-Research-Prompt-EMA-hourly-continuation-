# EMA Hourly Continuation — BTT/USDT P12_21

**Symbol:** BTT/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1569 |
| net_profit_factor | 0.1448 |
| net_win_rate | 0.2677 |
| gross_profit_factor | 0.6358 |
| gross_win_rate | 0.3633 |
| sharpe_ratio | -22.2292 |
| sortino_ratio | -13.7657 |
| max_drawdown | 1.0000 |
| cagr | -0.9995 |
| net_avg_win | 4.0301 |
| net_avg_loss | -10.1763 |
| avg_hold_time_bars | 2.4289 |
| exposure | 0.1732 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
