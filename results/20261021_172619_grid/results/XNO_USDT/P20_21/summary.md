# EMA Hourly Continuation — XNO/USDT P20_21

**Symbol:** XNO/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 172 |
| net_profit_factor | 0.4040 |
| net_win_rate | 0.3547 |
| gross_profit_factor | 0.5805 |
| gross_win_rate | 0.3547 |
| sharpe_ratio | -3.7738 |
| sortino_ratio | -0.7040 |
| max_drawdown | 0.5656 |
| cagr | -0.2802 |
| net_avg_win | 62.4519 |
| net_avg_loss | -84.9612 |
| avg_hold_time_bars | 3.7442 |
| exposure | 0.0293 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
