# EMA Hourly Continuation — OP/USDT P12_26

**Symbol:** OP/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 418 |
| net_profit_factor | 0.7635 |
| net_win_rate | 0.5096 |
| gross_profit_factor | 1.0312 |
| gross_win_rate | 0.5096 |
| sharpe_ratio | -1.6825 |
| sortino_ratio | -0.4948 |
| max_drawdown | 0.4698 |
| cagr | -0.2033 |
| net_avg_win | 65.9330 |
| net_avg_loss | -89.7241 |
| avg_hold_time_bars | 5.6866 |
| exposure | 0.1080 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
