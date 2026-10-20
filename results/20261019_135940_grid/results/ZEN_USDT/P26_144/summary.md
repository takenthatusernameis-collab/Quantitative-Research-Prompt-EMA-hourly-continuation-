# EMA Hourly Continuation — ZEN/USDT P26_144

**Symbol:** ZEN/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 515 |
| net_profit_factor | 0.6530 |
| net_win_rate | 0.4757 |
| gross_profit_factor | 0.9735 |
| gross_win_rate | 0.4854 |
| sharpe_ratio | -3.1672 |
| sortino_ratio | -1.0083 |
| max_drawdown | 0.7304 |
| cagr | -0.3838 |
| net_avg_win | 54.0407 |
| net_avg_loss | -75.0970 |
| avg_hold_time_bars | 20.6039 |
| exposure | 0.4823 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
