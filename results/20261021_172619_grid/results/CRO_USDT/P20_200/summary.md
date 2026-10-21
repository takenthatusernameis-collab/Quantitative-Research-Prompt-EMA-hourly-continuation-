# EMA Hourly Continuation — CRO/USDT P20_200

**Symbol:** CRO/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 263 |
| net_profit_factor | 0.8078 |
| net_win_rate | 0.5209 |
| gross_profit_factor | 1.0651 |
| gross_win_rate | 0.5209 |
| sharpe_ratio | -0.9775 |
| sortino_ratio | -0.2280 |
| max_drawdown | 0.2627 |
| cagr | -0.0999 |
| net_avg_win | 71.2836 |
| net_avg_loss | -95.9451 |
| avg_hold_time_bars | 56.7833 |
| exposure | 0.6788 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
