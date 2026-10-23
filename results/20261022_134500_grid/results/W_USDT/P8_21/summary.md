# EMA Hourly Continuation — W/USDT P8_21

**Symbol:** W/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1647 |
| net_profit_factor | 0.5010 |
| net_win_rate | 0.4511 |
| gross_profit_factor | 0.9047 |
| gross_win_rate | 0.4675 |
| sharpe_ratio | -9.5408 |
| sortino_ratio | -5.4666 |
| max_drawdown | 0.9988 |
| cagr | -0.9311 |
| net_avg_win | 13.4989 |
| net_avg_loss | -22.1434 |
| avg_hold_time_bars | 2.9666 |
| exposure | 0.2221 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
