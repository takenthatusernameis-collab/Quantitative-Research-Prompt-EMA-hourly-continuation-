# EMA Hourly Continuation — JASMY/USDT P12_144

**Symbol:** JASMY/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 330 |
| net_profit_factor | 1.0561 |
| net_win_rate | 0.5576 |
| gross_profit_factor | 1.2491 |
| gross_win_rate | 0.5576 |
| sharpe_ratio | 0.3737 |
| sortino_ratio | 0.0988 |
| max_drawdown | 0.2016 |
| cagr | 0.0368 |
| net_avg_win | 97.3650 |
| net_avg_loss | -116.1929 |
| avg_hold_time_bars | 46.6545 |
| exposure | 0.6998 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
