# EMA Hourly Continuation — DIA/USDT P20_89

**Symbol:** DIA/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 518 |
| net_profit_factor | 0.7611 |
| net_win_rate | 0.4884 |
| gross_profit_factor | 0.9542 |
| gross_win_rate | 0.4884 |
| sharpe_ratio | -2.0014 |
| sortino_ratio | -0.6492 |
| max_drawdown | 0.5708 |
| cagr | -0.2590 |
| net_avg_win | 66.8067 |
| net_avg_loss | -83.7989 |
| avg_hold_time_bars | 15.9614 |
| exposure | 0.3741 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
