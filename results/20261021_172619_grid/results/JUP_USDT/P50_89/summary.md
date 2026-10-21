# EMA Hourly Continuation — JUP/USDT P50_89

**Symbol:** JUP/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 313 |
| net_profit_factor | 0.8398 |
| net_win_rate | 0.5240 |
| gross_profit_factor | 1.0806 |
| gross_win_rate | 0.5240 |
| sharpe_ratio | -0.8874 |
| sortino_ratio | -0.2261 |
| max_drawdown | 0.2874 |
| cagr | -0.0999 |
| net_avg_win | 74.2232 |
| net_avg_loss | -97.2808 |
| avg_hold_time_bars | 7.2460 |
| exposure | 0.1031 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
