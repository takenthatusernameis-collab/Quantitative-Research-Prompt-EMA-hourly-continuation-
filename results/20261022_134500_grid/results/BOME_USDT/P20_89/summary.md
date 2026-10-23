# EMA Hourly Continuation — BOME/USDT P20_89

**Symbol:** BOME/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 665 |
| net_profit_factor | 0.5688 |
| net_win_rate | 0.4541 |
| gross_profit_factor | 0.7972 |
| gross_win_rate | 0.4586 |
| sharpe_ratio | -4.1421 |
| sortino_ratio | -1.5011 |
| max_drawdown | 0.8488 |
| cagr | -0.5116 |
| net_avg_win | 36.4485 |
| net_avg_loss | -53.3155 |
| avg_hold_time_bars | 13.4165 |
| exposure | 0.4055 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
