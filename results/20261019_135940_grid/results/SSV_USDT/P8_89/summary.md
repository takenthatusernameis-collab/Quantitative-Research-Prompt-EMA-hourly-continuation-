# EMA Hourly Continuation — SSV/USDT P8_89

**Symbol:** SSV/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 641 |
| net_profit_factor | 0.6198 |
| net_win_rate | 0.4462 |
| gross_profit_factor | 0.8664 |
| gross_win_rate | 0.4540 |
| sharpe_ratio | -4.2651 |
| sortino_ratio | -1.5147 |
| max_drawdown | 0.8603 |
| cagr | -0.5132 |
| net_avg_win | 47.7339 |
| net_avg_loss | -62.0421 |
| avg_hold_time_bars | 23.7426 |
| exposure | 0.6887 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
