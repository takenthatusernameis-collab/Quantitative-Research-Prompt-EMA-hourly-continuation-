# EMA Hourly Continuation — SQD/USDT P8_21

**Symbol:** SQD/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1486 |
| net_profit_factor | 0.5158 |
| net_win_rate | 0.4287 |
| gross_profit_factor | 0.9087 |
| gross_win_rate | 0.4448 |
| sharpe_ratio | -10.0510 |
| sortino_ratio | -5.5100 |
| max_drawdown | 0.9988 |
| cagr | -0.9368 |
| net_avg_win | 16.6995 |
| net_avg_loss | -24.2937 |
| avg_hold_time_bars | 3.0067 |
| exposure | 0.2100 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
