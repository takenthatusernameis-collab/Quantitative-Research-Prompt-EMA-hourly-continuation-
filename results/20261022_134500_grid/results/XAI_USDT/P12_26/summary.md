# EMA Hourly Continuation — XAI/USDT P12_26

**Symbol:** XAI/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1498 |
| net_profit_factor | 0.5027 |
| net_win_rate | 0.4212 |
| gross_profit_factor | 0.9035 |
| gross_win_rate | 0.4406 |
| sharpe_ratio | -10.9272 |
| sortino_ratio | -5.9512 |
| max_drawdown | 0.9994 |
| cagr | -0.9491 |
| net_avg_win | 16.0107 |
| net_avg_loss | -23.1800 |
| avg_hold_time_bars | 3.0347 |
| exposure | 0.2066 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
