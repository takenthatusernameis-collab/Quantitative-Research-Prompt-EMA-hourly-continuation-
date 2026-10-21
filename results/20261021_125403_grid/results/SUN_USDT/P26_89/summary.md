# EMA Hourly Continuation — SUN/USDT P26_89

**Symbol:** SUN/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 440 |
| net_profit_factor | 0.4778 |
| net_win_rate | 0.4136 |
| gross_profit_factor | 0.7861 |
| gross_win_rate | 0.4250 |
| sharpe_ratio | -5.5226 |
| sortino_ratio | -1.6477 |
| max_drawdown | 0.8648 |
| cagr | -0.5449 |
| net_avg_win | 43.3803 |
| net_avg_loss | -64.0418 |
| avg_hold_time_bars | 15.9886 |
| exposure | 0.3184 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
