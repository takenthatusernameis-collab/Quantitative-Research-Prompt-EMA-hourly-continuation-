# EMA Hourly Continuation — MOCA/USDT P20_89

**Symbol:** MOCA/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 463 |
| net_profit_factor | 0.7692 |
| net_win_rate | 0.4946 |
| gross_profit_factor | 0.9826 |
| gross_win_rate | 0.4946 |
| sharpe_ratio | -1.9666 |
| sortino_ratio | -0.6351 |
| max_drawdown | 0.5204 |
| cagr | -0.2534 |
| net_avg_win | 70.7240 |
| net_avg_loss | -89.9822 |
| avg_hold_time_bars | 15.1965 |
| exposure | 0.3527 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
