# EMA Hourly Continuation — BCH/USDT P20_55

**Symbol:** BCH/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.6381 |
| net_win_rate | 0.4742 |
| gross_profit_factor | 0.9154 |
| gross_win_rate | 0.4742 |
| sharpe_ratio | -3.1702 |
| sortino_ratio | -0.9797 |
| max_drawdown | 0.6772 |
| cagr | -0.3609 |
| net_avg_win | 53.8566 |
| net_avg_loss | -76.1355 |
| avg_hold_time_bars | 10.6395 |
| exposure | 0.2254 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
