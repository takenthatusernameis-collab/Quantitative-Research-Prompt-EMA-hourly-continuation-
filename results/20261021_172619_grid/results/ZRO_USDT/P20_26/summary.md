# EMA Hourly Continuation — ZRO/USDT P20_26

**Symbol:** ZRO/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 146 |
| net_profit_factor | 0.7617 |
| net_win_rate | 0.4932 |
| gross_profit_factor | 0.9786 |
| gross_win_rate | 0.4932 |
| sharpe_ratio | -1.0951 |
| sortino_ratio | -0.1966 |
| max_drawdown | 0.2507 |
| cagr | -0.0867 |
| net_avg_win | 84.6151 |
| net_avg_loss | -108.0890 |
| avg_hold_time_bars | 4.6986 |
| exposure | 0.0336 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
