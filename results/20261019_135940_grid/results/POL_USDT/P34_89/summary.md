# EMA Hourly Continuation — POL/USDT P34_89

**Symbol:** POL/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 748 |
| net_profit_factor | 0.4016 |
| net_win_rate | 0.4532 |
| gross_profit_factor | 0.7388 |
| gross_win_rate | 0.4733 |
| sharpe_ratio | -6.0687 |
| sortino_ratio | -2.3204 |
| max_drawdown | 0.9449 |
| cagr | -0.6837 |
| net_avg_win | 18.6990 |
| net_avg_loss | -38.5908 |
| avg_hold_time_bars | 7.5963 |
| exposure | 0.2583 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
