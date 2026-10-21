# EMA Hourly Continuation — LTC/USDT P20_89

**Symbol:** LTC/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 460 |
| net_profit_factor | 0.5512 |
| net_win_rate | 0.4348 |
| gross_profit_factor | 0.7560 |
| gross_win_rate | 0.4348 |
| sharpe_ratio | -3.9107 |
| sortino_ratio | -1.1929 |
| max_drawdown | 0.7588 |
| cagr | -0.4231 |
| net_avg_win | 45.9745 |
| net_avg_loss | -64.1651 |
| avg_hold_time_bars | 16.6848 |
| exposure | 0.3489 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
