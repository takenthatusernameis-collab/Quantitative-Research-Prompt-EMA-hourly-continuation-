# EMA Hourly Continuation — NYM/USDT P21_200

**Symbol:** NYM/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.3627 |
| net_win_rate | 0.3648 |
| gross_profit_factor | 0.6386 |
| gross_win_rate | 0.3772 |
| sharpe_ratio | -6.3569 |
| sortino_ratio | -1.7935 |
| max_drawdown | 0.8980 |
| cagr | -0.5966 |
| net_avg_win | 34.7492 |
| net_avg_loss | -55.0194 |
| avg_hold_time_bars | 32.5385 |
| exposure | 0.5960 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
