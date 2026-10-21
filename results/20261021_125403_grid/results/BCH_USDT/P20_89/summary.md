# EMA Hourly Continuation — BCH/USDT P20_89

**Symbol:** BCH/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.6198 |
| net_win_rate | 0.4513 |
| gross_profit_factor | 0.8267 |
| gross_win_rate | 0.4513 |
| sharpe_ratio | -3.2641 |
| sortino_ratio | -0.9876 |
| max_drawdown | 0.6827 |
| cagr | -0.3646 |
| net_avg_win | 54.3379 |
| net_avg_loss | -72.1099 |
| avg_hold_time_bars | 17.7721 |
| exposure | 0.3651 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
