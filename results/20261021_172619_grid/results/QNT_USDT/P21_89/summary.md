# EMA Hourly Continuation — QNT/USDT P21_89

**Symbol:** QNT/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 564 |
| net_profit_factor | 0.7492 |
| net_win_rate | 0.5053 |
| gross_profit_factor | 1.0036 |
| gross_win_rate | 0.5053 |
| sharpe_ratio | -2.0449 |
| sortino_ratio | -0.6972 |
| max_drawdown | 0.5729 |
| cagr | -0.2736 |
| net_avg_win | 57.8410 |
| net_avg_loss | -78.8684 |
| avg_hold_time_bars | 12.6152 |
| exposure | 0.3234 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
