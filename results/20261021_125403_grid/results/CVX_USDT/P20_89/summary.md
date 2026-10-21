# EMA Hourly Continuation — CVX/USDT P20_89

**Symbol:** CVX/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 528 |
| net_profit_factor | 0.8092 |
| net_win_rate | 0.5019 |
| gross_profit_factor | 0.9976 |
| gross_win_rate | 0.5019 |
| sharpe_ratio | -1.4815 |
| sortino_ratio | -0.4876 |
| max_drawdown | 0.4480 |
| cagr | -0.2024 |
| net_avg_win | 69.3402 |
| net_avg_loss | -86.3457 |
| avg_hold_time_bars | 14.2443 |
| exposure | 0.3419 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
