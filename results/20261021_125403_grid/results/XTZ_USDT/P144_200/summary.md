# EMA Hourly Continuation — XTZ/USDT P144_200

**Symbol:** XTZ/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 211 |
| net_profit_factor | 0.5944 |
| net_win_rate | 0.4739 |
| gross_profit_factor | 0.8790 |
| gross_win_rate | 0.4739 |
| sharpe_ratio | -2.2247 |
| sortino_ratio | -0.4635 |
| max_drawdown | 0.4444 |
| cagr | -0.1914 |
| net_avg_win | 60.6072 |
| net_avg_loss | -91.8552 |
| avg_hold_time_bars | 6.3886 |
| exposure | 0.0613 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
