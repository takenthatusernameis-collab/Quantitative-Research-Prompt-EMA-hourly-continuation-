# EMA Hourly Continuation — CRO/USDT P20_200

**Symbol:** CRO/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.5586 |
| net_win_rate | 0.4841 |
| gross_profit_factor | 0.9443 |
| gross_win_rate | 0.4986 |
| sharpe_ratio | -2.9955 |
| sortino_ratio | -0.7730 |
| max_drawdown | 0.6290 |
| cagr | -0.3185 |
| net_avg_win | 46.8526 |
| net_avg_loss | -78.6865 |
| avg_hold_time_bars | 43.7101 |
| exposure | 0.6855 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
