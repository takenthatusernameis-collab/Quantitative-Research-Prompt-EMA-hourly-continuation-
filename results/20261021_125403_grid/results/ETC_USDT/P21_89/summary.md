# EMA Hourly Continuation — ETC/USDT P21_89

**Symbol:** ETC/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.6443 |
| net_win_rate | 0.4820 |
| gross_profit_factor | 0.9070 |
| gross_win_rate | 0.4820 |
| sharpe_ratio | -2.8707 |
| sortino_ratio | -0.9177 |
| max_drawdown | 0.6632 |
| cagr | -0.3432 |
| net_avg_win | 49.0122 |
| net_avg_loss | -70.7830 |
| avg_hold_time_bars | 14.5240 |
| exposure | 0.3301 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
