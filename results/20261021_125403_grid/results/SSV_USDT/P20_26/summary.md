# EMA Hourly Continuation — SSV/USDT P20_26

**Symbol:** SSV/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 274 |
| net_profit_factor | 0.7422 |
| net_win_rate | 0.5073 |
| gross_profit_factor | 1.0547 |
| gross_win_rate | 0.5073 |
| sharpe_ratio | -1.6742 |
| sortino_ratio | -0.3978 |
| max_drawdown | 0.3845 |
| cagr | -0.1666 |
| net_avg_win | 76.3081 |
| net_avg_loss | -105.8667 |
| avg_hold_time_bars | 4.7628 |
| exposure | 0.0591 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
