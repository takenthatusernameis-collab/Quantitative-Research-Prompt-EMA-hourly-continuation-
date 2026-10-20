# EMA Hourly Continuation — FIDA/USDT P50_89

**Symbol:** FIDA/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 685 |
| net_profit_factor | 0.4482 |
| net_win_rate | 0.4350 |
| gross_profit_factor | 0.7907 |
| gross_win_rate | 0.4453 |
| sharpe_ratio | -6.1242 |
| sortino_ratio | -2.2597 |
| max_drawdown | 0.9373 |
| cagr | -0.6639 |
| net_avg_win | 25.5185 |
| net_avg_loss | -43.8390 |
| avg_hold_time_bars | 4.8876 |
| exposure | 0.1515 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
