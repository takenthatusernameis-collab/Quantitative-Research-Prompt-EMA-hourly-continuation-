# EMA Hourly Continuation — API3/USDT P50_55

**Symbol:** API3/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 848 |
| net_profit_factor | 0.2418 |
| net_win_rate | 0.3514 |
| gross_profit_factor | 0.7352 |
| gross_win_rate | 0.4281 |
| sharpe_ratio | -11.9537 |
| sortino_ratio | -5.0753 |
| max_drawdown | 0.9988 |
| cagr | -0.9307 |
| net_avg_win | 10.6868 |
| net_avg_loss | -23.9498 |
| avg_hold_time_bars | 2.1450 |
| exposure | 0.0827 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
