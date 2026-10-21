# EMA Hourly Continuation — KNC/USDT P12_21

**Symbol:** KNC/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 600 |
| net_profit_factor | 0.5411 |
| net_win_rate | 0.4550 |
| gross_profit_factor | 0.9108 |
| gross_win_rate | 0.4550 |
| sharpe_ratio | -5.4589 |
| sortino_ratio | -1.9191 |
| max_drawdown | 0.8989 |
| cagr | -0.5912 |
| net_avg_win | 38.6168 |
| net_avg_loss | -59.5866 |
| avg_hold_time_bars | 5.2967 |
| exposure | 0.1445 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
