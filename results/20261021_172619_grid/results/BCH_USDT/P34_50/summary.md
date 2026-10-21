# EMA Hourly Continuation — BCH/USDT P34_50

**Symbol:** BCH/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 229 |
| net_profit_factor | 0.6322 |
| net_win_rate | 0.4847 |
| gross_profit_factor | 0.9539 |
| gross_win_rate | 0.4847 |
| sharpe_ratio | -2.1975 |
| sortino_ratio | -0.4780 |
| max_drawdown | 0.4550 |
| cagr | -0.1944 |
| net_avg_win | 64.8661 |
| net_avg_loss | -96.5194 |
| avg_hold_time_bars | 6.4934 |
| exposure | 0.0676 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
