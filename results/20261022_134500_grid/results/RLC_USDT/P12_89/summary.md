# EMA Hourly Continuation — RLC/USDT P12_89

**Symbol:** RLC/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 558 |
| net_profit_factor | 0.7478 |
| net_win_rate | 0.5197 |
| gross_profit_factor | 1.1061 |
| gross_win_rate | 0.5251 |
| sharpe_ratio | -2.2912 |
| sortino_ratio | -0.7608 |
| max_drawdown | 0.6409 |
| cagr | -0.3079 |
| net_avg_win | 61.6799 |
| net_avg_loss | -89.2518 |
| avg_hold_time_bars | 24.6792 |
| exposure | 0.6260 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
