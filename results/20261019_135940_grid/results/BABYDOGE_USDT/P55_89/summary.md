# EMA Hourly Continuation — BABYDOGE/USDT P55_89

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 14 |
| net_profit_factor | 0.9013 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9897 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -0.1099 |
| sortino_ratio | -0.0059 |
| max_drawdown | 0.0330 |
| cagr | -0.0029 |
| net_avg_win | 93.9502 |
| net_avg_loss | -104.2389 |
| avg_hold_time_bars | 27.0000 |
| exposure | 0.0171 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
