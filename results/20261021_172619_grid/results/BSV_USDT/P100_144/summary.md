# EMA Hourly Continuation — BSV/USDT P100_144

**Symbol:** BSV/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 241 |
| net_profit_factor | 0.5471 |
| net_win_rate | 0.4440 |
| gross_profit_factor | 0.8002 |
| gross_win_rate | 0.4440 |
| sharpe_ratio | -2.9137 |
| sortino_ratio | -0.6467 |
| max_drawdown | 0.5313 |
| cagr | -0.2579 |
| net_avg_win | 59.5162 |
| net_avg_loss | -86.8683 |
| avg_hold_time_bars | 6.9544 |
| exposure | 0.0762 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
