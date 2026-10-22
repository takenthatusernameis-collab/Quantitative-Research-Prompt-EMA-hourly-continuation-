# EMA Hourly Continuation — SEI/USDT P50_55

**Symbol:** SEI/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 796 |
| net_profit_factor | 0.2653 |
| net_win_rate | 0.3543 |
| gross_profit_factor | 0.6307 |
| gross_win_rate | 0.3882 |
| sharpe_ratio | -12.1663 |
| sortino_ratio | -5.0409 |
| max_drawdown | 0.9991 |
| cagr | -0.9371 |
| net_avg_win | 12.7921 |
| net_avg_loss | -26.4547 |
| avg_hold_time_bars | 1.7626 |
| exposure | 0.0638 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
