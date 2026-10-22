# EMA Hourly Continuation — WIF/USDT P20_100

**Symbol:** WIF/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 686 |
| net_profit_factor | 0.6527 |
| net_win_rate | 0.4723 |
| gross_profit_factor | 0.9067 |
| gross_win_rate | 0.4781 |
| sharpe_ratio | -3.7744 |
| sortino_ratio | -1.3886 |
| max_drawdown | 0.8134 |
| cagr | -0.4856 |
| net_avg_win | 47.0861 |
| net_avg_loss | -64.5638 |
| avg_hold_time_bars | 13.1122 |
| exposure | 0.4089 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
