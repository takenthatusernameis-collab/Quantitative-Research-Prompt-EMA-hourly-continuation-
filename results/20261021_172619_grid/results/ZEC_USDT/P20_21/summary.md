# EMA Hourly Continuation — ZEC/USDT P20_21

**Symbol:** ZEC/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 104 |
| net_profit_factor | 0.7036 |
| net_win_rate | 0.4808 |
| gross_profit_factor | 0.9242 |
| gross_win_rate | 0.4808 |
| sharpe_ratio | -1.1125 |
| sortino_ratio | -0.1622 |
| max_drawdown | 0.2217 |
| cagr | -0.0718 |
| net_avg_win | 80.9654 |
| net_avg_loss | -106.5503 |
| avg_hold_time_bars | 4.7308 |
| exposure | 0.0224 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
