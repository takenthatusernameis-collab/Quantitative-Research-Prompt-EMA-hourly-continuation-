# EMA Hourly Continuation — BCH/USDT P55_89

**Symbol:** BCH/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.5978 |
| net_win_rate | 0.4769 |
| gross_profit_factor | 0.8723 |
| gross_win_rate | 0.4769 |
| sharpe_ratio | -2.4648 |
| sortino_ratio | -0.5928 |
| max_drawdown | 0.5231 |
| cagr | -0.2374 |
| net_avg_win | 54.7474 |
| net_avg_loss | -83.4872 |
| avg_hold_time_bars | 6.4982 |
| exposure | 0.0830 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
