# EMA Hourly Continuation — QNT/USDT P20_89

**Symbol:** QNT/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 880 |
| net_profit_factor | 0.5356 |
| net_win_rate | 0.4705 |
| gross_profit_factor | 0.9284 |
| gross_win_rate | 0.4830 |
| sharpe_ratio | -5.7624 |
| sortino_ratio | -2.4027 |
| max_drawdown | 0.9497 |
| cagr | -0.6907 |
| net_avg_win | 26.4002 |
| net_avg_loss | -43.7870 |
| avg_hold_time_bars | 8.7364 |
| exposure | 0.3495 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
