# EMA Hourly Continuation — XAI/USDT P12_144

**Symbol:** XAI/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.8320 |
| net_win_rate | 0.4883 |
| gross_profit_factor | 0.9733 |
| gross_win_rate | 0.4883 |
| sharpe_ratio | -1.2064 |
| sortino_ratio | -0.3184 |
| max_drawdown | 0.4367 |
| cagr | -0.1383 |
| net_avg_win | 92.4800 |
| net_avg_loss | -106.0690 |
| avg_hold_time_bars | 45.9883 |
| exposure | 0.7149 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
