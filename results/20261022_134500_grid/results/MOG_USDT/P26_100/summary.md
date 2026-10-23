# EMA Hourly Continuation — MOG/USDT P26_100

**Symbol:** MOG/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 617 |
| net_profit_factor | 0.6409 |
| net_win_rate | 0.4603 |
| gross_profit_factor | 0.8484 |
| gross_win_rate | 0.4652 |
| sharpe_ratio | -3.8778 |
| sortino_ratio | -1.4132 |
| max_drawdown | 0.8039 |
| cagr | -0.4907 |
| net_avg_win | 49.5077 |
| net_avg_loss | -65.8760 |
| avg_hold_time_bars | 10.4635 |
| exposure | 0.3209 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
