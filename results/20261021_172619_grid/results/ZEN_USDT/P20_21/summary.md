# EMA Hourly Continuation — ZEN/USDT P20_21

**Symbol:** ZEN/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 153 |
| net_profit_factor | 0.6182 |
| net_win_rate | 0.4771 |
| gross_profit_factor | 0.9203 |
| gross_win_rate | 0.4771 |
| sharpe_ratio | -1.8540 |
| sortino_ratio | -0.3285 |
| max_drawdown | 0.3258 |
| cagr | -0.1398 |
| net_avg_win | 69.8440 |
| net_avg_loss | -103.0966 |
| avg_hold_time_bars | 5.3464 |
| exposure | 0.0372 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
