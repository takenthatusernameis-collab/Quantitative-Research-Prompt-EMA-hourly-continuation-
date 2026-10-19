# EMA Hourly Continuation — JASMY/USDT P12_89

**Symbol:** JASMY/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 685 |
| net_profit_factor | 0.7107 |
| net_win_rate | 0.4993 |
| gross_profit_factor | 1.0240 |
| gross_win_rate | 0.5080 |
| sharpe_ratio | -2.9897 |
| sortino_ratio | -1.1053 |
| max_drawdown | 0.7645 |
| cagr | -0.4095 |
| net_avg_win | 52.6829 |
| net_avg_loss | -73.9172 |
| avg_hold_time_bars | 17.6978 |
| exposure | 0.5510 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
