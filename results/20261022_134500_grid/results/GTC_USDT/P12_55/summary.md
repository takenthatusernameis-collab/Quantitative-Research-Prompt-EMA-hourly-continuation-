# EMA Hourly Continuation — GTC/USDT P12_55

**Symbol:** GTC/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 933 |
| net_profit_factor | 0.6012 |
| net_win_rate | 0.4598 |
| gross_profit_factor | 0.9413 |
| gross_win_rate | 0.4684 |
| sharpe_ratio | -5.5727 |
| sortino_ratio | -2.3961 |
| max_drawdown | 0.9471 |
| cagr | -0.6813 |
| net_avg_win | 33.1543 |
| net_avg_loss | -46.9392 |
| avg_hold_time_bars | 8.9378 |
| exposure | 0.3790 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
