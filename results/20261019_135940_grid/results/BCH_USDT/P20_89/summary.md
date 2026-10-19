# EMA Hourly Continuation — BCH/USDT P20_89

**Symbol:** BCH/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 714 |
| net_profit_factor | 0.4847 |
| net_win_rate | 0.4412 |
| gross_profit_factor | 0.8263 |
| gross_win_rate | 0.4538 |
| sharpe_ratio | -6.2646 |
| sortino_ratio | -2.3653 |
| max_drawdown | 0.9436 |
| cagr | -0.6809 |
| net_avg_win | 28.1620 |
| net_avg_loss | -45.8729 |
| avg_hold_time_bars | 11.9118 |
| exposure | 0.3866 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
