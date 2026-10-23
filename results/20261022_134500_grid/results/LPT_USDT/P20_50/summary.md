# EMA Hourly Continuation — LPT/USDT P20_50

**Symbol:** LPT/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1077 |
| net_profit_factor | 0.4817 |
| net_win_rate | 0.4197 |
| gross_profit_factor | 0.8101 |
| gross_win_rate | 0.4448 |
| sharpe_ratio | -8.5738 |
| sortino_ratio | -3.9669 |
| max_drawdown | 0.9929 |
| cagr | -0.8568 |
| net_avg_win | 20.4050 |
| net_avg_loss | -30.6354 |
| avg_hold_time_bars | 4.7539 |
| exposure | 0.2327 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
