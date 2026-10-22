# EMA Hourly Continuation — SYN/USDT P20_26

**Symbol:** SYN/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 289 |
| net_profit_factor | 0.6092 |
| net_win_rate | 0.4567 |
| gross_profit_factor | 0.8686 |
| gross_win_rate | 0.4567 |
| sharpe_ratio | -2.8092 |
| sortino_ratio | -0.6827 |
| max_drawdown | 0.5643 |
| cagr | -0.2691 |
| net_avg_win | 64.3487 |
| net_avg_loss | -88.8077 |
| avg_hold_time_bars | 4.2837 |
| exposure | 0.0563 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
