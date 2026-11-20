# EMA Hourly Continuation — P2P/USDT P26_50

**Symbol:** P2P/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 874 |
| net_profit_factor | 0.3576 |
| net_win_rate | 0.3444 |
| gross_profit_factor | 0.5877 |
| gross_win_rate | 0.3467 |
| sharpe_ratio | -9.4469 |
| sortino_ratio | -3.9235 |
| max_drawdown | 0.9926 |
| cagr | -0.8579 |
| net_avg_win | 18.3528 |
| net_avg_loss | -26.9629 |
| avg_hold_time_bars | 4.6670 |
| exposure | 0.1854 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
