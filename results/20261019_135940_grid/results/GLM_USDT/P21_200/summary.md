# EMA Hourly Continuation — GLM/USDT P21_200

**Symbol:** GLM/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 447 |
| net_profit_factor | 0.6085 |
| net_win_rate | 0.4586 |
| gross_profit_factor | 0.8577 |
| gross_win_rate | 0.4631 |
| sharpe_ratio | -3.2542 |
| sortino_ratio | -0.9736 |
| max_drawdown | 0.6886 |
| cagr | -0.3679 |
| net_avg_win | 51.8517 |
| net_avg_loss | -72.1863 |
| avg_hold_time_bars | 30.0783 |
| exposure | 0.6111 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
