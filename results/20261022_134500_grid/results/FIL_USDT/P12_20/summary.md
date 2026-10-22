# EMA Hourly Continuation — FIL/USDT P12_20

**Symbol:** FIL/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1501 |
| net_profit_factor | 0.2115 |
| net_win_rate | 0.3797 |
| gross_profit_factor | 0.6692 |
| gross_win_rate | 0.4111 |
| sharpe_ratio | -15.2665 |
| sortino_ratio | -8.5096 |
| max_drawdown | 1.0000 |
| cagr | -0.9888 |
| net_avg_win | 4.7071 |
| net_avg_loss | -13.6229 |
| avg_hold_time_bars | 2.0620 |
| exposure | 0.1407 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
