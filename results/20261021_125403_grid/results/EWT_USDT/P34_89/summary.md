# EMA Hourly Continuation — EWT/USDT P34_89

**Symbol:** EWT/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.7144 |
| net_win_rate | 0.4744 |
| gross_profit_factor | 0.9052 |
| gross_win_rate | 0.4744 |
| sharpe_ratio | -2.0781 |
| sortino_ratio | -0.5704 |
| max_drawdown | 0.5015 |
| cagr | -0.2310 |
| net_avg_win | 68.6434 |
| net_avg_loss | -86.7183 |
| avg_hold_time_bars | 10.4825 |
| exposure | 0.1768 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
