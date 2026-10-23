# EMA Hourly Continuation — AMP/USDT P20_50

**Symbol:** AMP/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1417 |
| net_profit_factor | 0.3358 |
| net_win_rate | 0.3691 |
| gross_profit_factor | 0.7176 |
| gross_win_rate | 0.3910 |
| sharpe_ratio | -13.3691 |
| sortino_ratio | -7.1654 |
| max_drawdown | 0.9999 |
| cagr | -0.9725 |
| net_avg_win | 9.6645 |
| net_avg_loss | -16.8382 |
| avg_hold_time_bars | 3.8723 |
| exposure | 0.2494 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
