# EMA Hourly Continuation — REZ/USDT P34_200

**Symbol:** REZ/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.9762 |
| net_win_rate | 0.5355 |
| gross_profit_factor | 1.1437 |
| gross_win_rate | 0.5355 |
| sharpe_ratio | -0.0902 |
| sortino_ratio | -0.0231 |
| max_drawdown | 0.2074 |
| cagr | -0.0163 |
| net_avg_win | 98.8795 |
| net_avg_loss | -116.7591 |
| avg_hold_time_bars | 37.1742 |
| exposure | 0.5317 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
