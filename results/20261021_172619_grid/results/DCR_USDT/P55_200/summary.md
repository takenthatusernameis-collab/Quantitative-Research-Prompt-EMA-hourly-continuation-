# EMA Hourly Continuation — DCR/USDT P55_200

**Symbol:** DCR/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.6751 |
| net_win_rate | 0.4688 |
| gross_profit_factor | 0.8876 |
| gross_win_rate | 0.4688 |
| sharpe_ratio | -2.2765 |
| sortino_ratio | -0.6062 |
| max_drawdown | 0.5273 |
| cagr | -0.2435 |
| net_avg_win | 63.6425 |
| net_avg_loss | -83.1806 |
| avg_hold_time_bars | 20.4062 |
| exposure | 0.3250 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
