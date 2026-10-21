# EMA Hourly Continuation — ETH/USDT P12_50

**Symbol:** ETH/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 545 |
| net_profit_factor | 0.6259 |
| net_win_rate | 0.4862 |
| gross_profit_factor | 0.9181 |
| gross_win_rate | 0.4862 |
| sharpe_ratio | -3.1663 |
| sortino_ratio | -1.0588 |
| max_drawdown | 0.7067 |
| cagr | -0.3842 |
| net_avg_win | 44.4460 |
| net_avg_loss | -67.2101 |
| avg_hold_time_bars | 12.3358 |
| exposure | 0.3056 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
