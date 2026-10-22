# EMA Hourly Continuation — SKY/USDT P8_21

**Symbol:** SKY/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1249 |
| net_profit_factor | 0.3967 |
| net_win_rate | 0.4388 |
| gross_profit_factor | 0.9065 |
| gross_win_rate | 0.4684 |
| sharpe_ratio | -11.2515 |
| sortino_ratio | -6.2293 |
| max_drawdown | 0.9984 |
| cagr | -0.9561 |
| net_avg_win | 11.9780 |
| net_avg_loss | -23.6053 |
| avg_hold_time_bars | 3.2578 |
| exposure | 0.2269 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
