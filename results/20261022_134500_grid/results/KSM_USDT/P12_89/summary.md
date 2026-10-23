# EMA Hourly Continuation — KSM/USDT P12_89

**Symbol:** KSM/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 674 |
| net_profit_factor | 0.5922 |
| net_win_rate | 0.4570 |
| gross_profit_factor | 0.9087 |
| gross_win_rate | 0.4659 |
| sharpe_ratio | -4.7475 |
| sortino_ratio | -1.7342 |
| max_drawdown | 0.8800 |
| cagr | -0.5625 |
| net_avg_win | 41.2332 |
| net_avg_loss | -58.5939 |
| avg_hold_time_bars | 18.6395 |
| exposure | 0.5710 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
