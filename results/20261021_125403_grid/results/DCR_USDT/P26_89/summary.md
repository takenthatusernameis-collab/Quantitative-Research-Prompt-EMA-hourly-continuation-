# EMA Hourly Continuation — DCR/USDT P26_89

**Symbol:** DCR/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 543 |
| net_profit_factor | 0.5900 |
| net_win_rate | 0.4475 |
| gross_profit_factor | 0.7902 |
| gross_win_rate | 0.4475 |
| sharpe_ratio | -3.6109 |
| sortino_ratio | -1.1929 |
| max_drawdown | 0.7596 |
| cagr | -0.4231 |
| net_avg_win | 44.4335 |
| net_avg_loss | -61.0030 |
| avg_hold_time_bars | 11.6317 |
| exposure | 0.2858 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
