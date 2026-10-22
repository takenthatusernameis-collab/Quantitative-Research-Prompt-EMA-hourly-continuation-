# EMA Hourly Continuation — TIA/USDT P12_144

**Symbol:** TIA/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 419 |
| net_profit_factor | 0.7203 |
| net_win_rate | 0.4773 |
| gross_profit_factor | 0.9369 |
| gross_win_rate | 0.4821 |
| sharpe_ratio | -2.2156 |
| sortino_ratio | -0.6428 |
| max_drawdown | 0.5712 |
| cagr | -0.2591 |
| net_avg_win | 68.1269 |
| net_avg_loss | -86.3769 |
| avg_hold_time_bars | 36.4320 |
| exposure | 0.6939 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
