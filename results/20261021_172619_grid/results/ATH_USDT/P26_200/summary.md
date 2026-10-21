# EMA Hourly Continuation — ATH/USDT P26_200

**Symbol:** ATH/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 301 |
| net_profit_factor | 1.0922 |
| net_win_rate | 0.5648 |
| gross_profit_factor | 1.2771 |
| gross_win_rate | 0.5648 |
| sharpe_ratio | 0.5605 |
| sortino_ratio | 0.1464 |
| max_drawdown | 0.1034 |
| cagr | 0.0584 |
| net_avg_win | 99.5710 |
| net_avg_loss | -118.3034 |
| avg_hold_time_bars | 38.1794 |
| exposure | 0.5570 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
