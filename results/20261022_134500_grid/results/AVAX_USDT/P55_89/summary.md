# EMA Hourly Continuation — AVAX/USDT P55_89

**Symbol:** AVAX/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 635 |
| net_profit_factor | 0.4736 |
| net_win_rate | 0.4331 |
| gross_profit_factor | 0.8961 |
| gross_win_rate | 0.4535 |
| sharpe_ratio | -7.0403 |
| sortino_ratio | -2.4847 |
| max_drawdown | 0.9617 |
| cagr | -0.7237 |
| net_avg_win | 31.4242 |
| net_avg_loss | -50.6836 |
| avg_hold_time_bars | 3.7118 |
| exposure | 0.1071 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
