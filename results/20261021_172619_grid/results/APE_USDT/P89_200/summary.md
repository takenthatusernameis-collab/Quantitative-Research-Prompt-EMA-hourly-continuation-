# EMA Hourly Continuation — APE/USDT P89_200

**Symbol:** APE/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 274 |
| net_profit_factor | 0.7796 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9763 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.1405 |
| sortino_ratio | -0.2707 |
| max_drawdown | 0.2944 |
| cagr | -0.1175 |
| net_avg_win | 69.5509 |
| net_avg_loss | -89.2088 |
| avg_hold_time_bars | 14.4197 |
| exposure | 0.1796 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
