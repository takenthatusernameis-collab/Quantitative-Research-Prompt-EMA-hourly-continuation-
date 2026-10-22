# EMA Hourly Continuation — ZRO/USDT P20_50

**Symbol:** ZRO/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 967 |
| net_profit_factor | 0.6183 |
| net_win_rate | 0.4850 |
| gross_profit_factor | 0.9946 |
| gross_win_rate | 0.4912 |
| sharpe_ratio | -5.1915 |
| sortino_ratio | -2.3518 |
| max_drawdown | 0.9308 |
| cagr | -0.6779 |
| net_avg_win | 32.0860 |
| net_avg_loss | -48.8682 |
| avg_hold_time_bars | 4.6060 |
| exposure | 0.2180 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
