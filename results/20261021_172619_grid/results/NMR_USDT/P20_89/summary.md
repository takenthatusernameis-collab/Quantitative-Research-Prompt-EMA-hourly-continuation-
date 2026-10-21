# EMA Hourly Continuation — NMR/USDT P20_89

**Symbol:** NMR/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 545 |
| net_profit_factor | 0.7373 |
| net_win_rate | 0.4881 |
| gross_profit_factor | 0.9491 |
| gross_win_rate | 0.4881 |
| sharpe_ratio | -2.3415 |
| sortino_ratio | -0.7801 |
| max_drawdown | 0.6104 |
| cagr | -0.3012 |
| net_avg_win | 62.5972 |
| net_avg_loss | -80.9486 |
| avg_hold_time_bars | 15.5798 |
| exposure | 0.3860 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
