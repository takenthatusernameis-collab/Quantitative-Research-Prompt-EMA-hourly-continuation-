# EMA Hourly Continuation — CHR/USDT P55_89

**Symbol:** CHR/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 722 |
| net_profit_factor | 0.4707 |
| net_win_rate | 0.4335 |
| gross_profit_factor | 0.7944 |
| gross_win_rate | 0.4418 |
| sharpe_ratio | -6.3571 |
| sortino_ratio | -2.4242 |
| max_drawdown | 0.9474 |
| cagr | -0.6850 |
| net_avg_win | 26.8673 |
| net_avg_loss | -43.6847 |
| avg_hold_time_bars | 4.2715 |
| exposure | 0.1396 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
