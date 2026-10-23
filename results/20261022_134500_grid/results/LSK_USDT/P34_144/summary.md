# EMA Hourly Continuation — LSK/USDT P34_144

**Symbol:** LSK/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 441 |
| net_profit_factor | 0.6357 |
| net_win_rate | 0.4785 |
| gross_profit_factor | 0.9479 |
| gross_win_rate | 0.4875 |
| sharpe_ratio | -2.8949 |
| sortino_ratio | -0.8556 |
| max_drawdown | 0.6752 |
| cagr | -0.3344 |
| net_avg_win | 52.9603 |
| net_avg_loss | -76.4221 |
| avg_hold_time_bars | 20.7732 |
| exposure | 0.4164 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
