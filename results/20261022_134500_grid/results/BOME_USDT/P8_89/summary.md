# EMA Hourly Continuation — BOME/USDT P8_89

**Symbol:** BOME/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 743 |
| net_profit_factor | 0.5608 |
| net_win_rate | 0.4603 |
| gross_profit_factor | 0.7975 |
| gross_win_rate | 0.4697 |
| sharpe_ratio | -4.0019 |
| sortino_ratio | -1.5313 |
| max_drawdown | 0.8530 |
| cagr | -0.5186 |
| net_avg_win | 31.3813 |
| net_avg_loss | -47.7259 |
| avg_hold_time_bars | 18.4240 |
| exposure | 0.6222 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
