# EMA Hourly Continuation — BOME/USDT P34_89

**Symbol:** BOME/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 710 |
| net_profit_factor | 0.5432 |
| net_win_rate | 0.4676 |
| gross_profit_factor | 0.8117 |
| gross_win_rate | 0.4718 |
| sharpe_ratio | -4.2095 |
| sortino_ratio | -1.5759 |
| max_drawdown | 0.8569 |
| cagr | -0.5312 |
| net_avg_win | 30.4785 |
| net_avg_loss | -49.2778 |
| avg_hold_time_bars | 7.0155 |
| exposure | 0.2264 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
