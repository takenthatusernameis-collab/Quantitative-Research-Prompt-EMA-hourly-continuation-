# EMA Hourly Continuation — TIA/USDT P34_89

**Symbol:** TIA/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 643 |
| net_profit_factor | 0.6909 |
| net_win_rate | 0.4821 |
| gross_profit_factor | 0.9929 |
| gross_win_rate | 0.4883 |
| sharpe_ratio | -3.4241 |
| sortino_ratio | -1.2231 |
| max_drawdown | 0.7771 |
| cagr | -0.4423 |
| net_avg_win | 55.4629 |
| net_avg_loss | -74.7337 |
| avg_hold_time_bars | 8.2582 |
| exposure | 0.2414 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
