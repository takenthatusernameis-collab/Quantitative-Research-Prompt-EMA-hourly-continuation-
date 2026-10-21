# EMA Hourly Continuation — DUSK/USDT P20_34

**Symbol:** DUSK/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.6434 |
| net_win_rate | 0.4629 |
| gross_profit_factor | 0.8871 |
| gross_win_rate | 0.4629 |
| sharpe_ratio | -2.9499 |
| sortino_ratio | -0.8467 |
| max_drawdown | 0.6671 |
| cagr | -0.3218 |
| net_avg_win | 60.1050 |
| net_avg_loss | -80.4992 |
| avg_hold_time_bars | 4.6040 |
| exposure | 0.0845 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
