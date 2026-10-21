# EMA Hourly Continuation — POKT/USDT P12_20

**Symbol:** POKT/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.5346 |
| net_win_rate | 0.3934 |
| gross_profit_factor | 0.7578 |
| gross_win_rate | 0.3956 |
| sharpe_ratio | -5.0812 |
| sortino_ratio | -1.5346 |
| max_drawdown | 0.8438 |
| cagr | -0.5085 |
| net_avg_win | 53.4705 |
| net_avg_loss | -64.8704 |
| avg_hold_time_bars | 5.2923 |
| exposure | 0.1090 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
