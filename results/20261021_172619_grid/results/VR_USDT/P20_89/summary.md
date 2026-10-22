# EMA Hourly Continuation — VR/USDT P20_89

**Symbol:** VR/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.6449 |
| net_win_rate | 0.4476 |
| gross_profit_factor | 0.8014 |
| gross_win_rate | 0.4476 |
| sharpe_ratio | -2.7072 |
| sortino_ratio | -0.7570 |
| max_drawdown | 0.5946 |
| cagr | -0.2970 |
| net_avg_win | 60.9308 |
| net_avg_loss | -76.5520 |
| avg_hold_time_bars | 19.1637 |
| exposure | 0.3406 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
