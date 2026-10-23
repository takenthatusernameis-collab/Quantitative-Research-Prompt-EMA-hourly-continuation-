# EMA Hourly Continuation — UQC/USDT P12_20

**Symbol:** UQC/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 578 |
| net_profit_factor | 0.0749 |
| net_win_rate | 0.1920 |
| gross_profit_factor | 0.2620 |
| gross_win_rate | 0.2405 |
| sharpe_ratio | -13.6170 |
| sortino_ratio | -4.9633 |
| max_drawdown | 0.9991 |
| cagr | -0.9388 |
| net_avg_win | 7.2847 |
| net_avg_loss | -23.1262 |
| avg_hold_time_bars | 20.3997 |
| exposure | 0.5337 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
