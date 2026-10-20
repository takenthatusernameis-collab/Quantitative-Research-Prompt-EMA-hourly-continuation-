# EMA Hourly Continuation — ENJ/USDT P34_89

**Symbol:** ENJ/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 705 |
| net_profit_factor | 0.6628 |
| net_win_rate | 0.4950 |
| gross_profit_factor | 1.1037 |
| gross_win_rate | 0.5121 |
| sharpe_ratio | -3.9353 |
| sortino_ratio | -1.4732 |
| max_drawdown | 0.8444 |
| cagr | -0.5068 |
| net_avg_win | 46.7698 |
| net_avg_loss | -69.1786 |
| avg_hold_time_bars | 7.7489 |
| exposure | 0.2483 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
