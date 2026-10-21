# EMA Hourly Continuation — FLR/USDT P20_55

**Symbol:** FLR/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 547 |
| net_profit_factor | 0.6217 |
| net_win_rate | 0.4625 |
| gross_profit_factor | 0.8637 |
| gross_win_rate | 0.4644 |
| sharpe_ratio | -3.6313 |
| sortino_ratio | -1.2130 |
| max_drawdown | 0.7625 |
| cagr | -0.4250 |
| net_avg_win | 48.7651 |
| net_avg_loss | -67.5037 |
| avg_hold_time_bars | 7.9890 |
| exposure | 0.1986 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
