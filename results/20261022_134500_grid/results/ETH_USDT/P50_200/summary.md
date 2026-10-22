# EMA Hourly Continuation — ETH/USDT P50_200

**Symbol:** ETH/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 351 |
| net_profit_factor | 0.5276 |
| net_win_rate | 0.4815 |
| gross_profit_factor | 0.9668 |
| gross_win_rate | 0.4957 |
| sharpe_ratio | -3.5245 |
| sortino_ratio | -0.9346 |
| max_drawdown | 0.6857 |
| cagr | -0.3586 |
| net_avg_win | 44.4285 |
| net_avg_loss | -78.1898 |
| avg_hold_time_bars | 25.5556 |
| exposure | 0.4077 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
