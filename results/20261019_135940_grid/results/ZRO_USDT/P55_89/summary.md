# EMA Hourly Continuation — ZRO/USDT P55_89

**Symbol:** ZRO/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 625 |
| net_profit_factor | 0.5661 |
| net_win_rate | 0.4816 |
| gross_profit_factor | 0.8916 |
| gross_win_rate | 0.4832 |
| sharpe_ratio | -4.2455 |
| sortino_ratio | -1.5544 |
| max_drawdown | 0.8437 |
| cagr | -0.5263 |
| net_avg_win | 35.7501 |
| net_avg_loss | -58.6718 |
| avg_hold_time_bars | 3.8768 |
| exposure | 0.1186 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
