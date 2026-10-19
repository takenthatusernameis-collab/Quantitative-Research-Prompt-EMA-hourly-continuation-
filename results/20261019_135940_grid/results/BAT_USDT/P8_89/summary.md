# EMA Hourly Continuation — BAT/USDT P8_89

**Symbol:** BAT/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 691 |
| net_profit_factor | 0.6268 |
| net_win_rate | 0.4834 |
| gross_profit_factor | 0.9888 |
| gross_win_rate | 0.4935 |
| sharpe_ratio | -3.6736 |
| sortino_ratio | -1.3512 |
| max_drawdown | 0.8197 |
| cagr | -0.4790 |
| net_avg_win | 40.5108 |
| net_avg_loss | -60.4654 |
| avg_hold_time_bars | 20.5384 |
| exposure | 0.6451 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
