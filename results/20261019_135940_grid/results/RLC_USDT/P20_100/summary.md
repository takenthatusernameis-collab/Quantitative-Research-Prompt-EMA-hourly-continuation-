# EMA Hourly Continuation — RLC/USDT P20_100

**Symbol:** RLC/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 681 |
| net_profit_factor | 0.6710 |
| net_win_rate | 0.4890 |
| gross_profit_factor | 1.0093 |
| gross_win_rate | 0.5022 |
| sharpe_ratio | -3.4173 |
| sortino_ratio | -1.2630 |
| max_drawdown | 0.7944 |
| cagr | -0.4494 |
| net_avg_win | 47.5583 |
| net_avg_loss | -67.8231 |
| avg_hold_time_bars | 13.4229 |
| exposure | 0.4155 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
