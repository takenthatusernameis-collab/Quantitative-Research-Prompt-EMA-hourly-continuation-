# EMA Hourly Continuation — SEI/USDT P20_21

**Symbol:** SEI/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 125 |
| net_profit_factor | 0.5805 |
| net_win_rate | 0.4400 |
| gross_profit_factor | 0.7966 |
| gross_win_rate | 0.4400 |
| sharpe_ratio | -1.9459 |
| sortino_ratio | -0.3101 |
| max_drawdown | 0.3207 |
| cagr | -0.1331 |
| net_avg_win | 75.8348 |
| net_avg_loss | -102.6431 |
| avg_hold_time_bars | 4.5040 |
| exposure | 0.0256 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
