# EMA Hourly Continuation — WIN/USDT P20_89

**Symbol:** WIN/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 650 |
| net_profit_factor | 0.4395 |
| net_win_rate | 0.4369 |
| gross_profit_factor | 0.8028 |
| gross_win_rate | 0.4523 |
| sharpe_ratio | -6.4276 |
| sortino_ratio | -2.3065 |
| max_drawdown | 0.9461 |
| cagr | -0.6853 |
| net_avg_win | 26.0906 |
| net_avg_loss | -46.0688 |
| avg_hold_time_bars | 13.7492 |
| exposure | 0.4062 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
