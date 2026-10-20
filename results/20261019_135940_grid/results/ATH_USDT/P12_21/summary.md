# EMA Hourly Continuation — ATH/USDT P12_21

**Symbol:** ATH/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1351 |
| net_profit_factor | 0.3537 |
| net_win_rate | 0.4130 |
| gross_profit_factor | 0.7444 |
| gross_win_rate | 0.4367 |
| sharpe_ratio | -12.0009 |
| sortino_ratio | -6.4570 |
| max_drawdown | 0.9996 |
| cagr | -0.9623 |
| net_avg_win | 9.8012 |
| net_avg_loss | -19.5015 |
| avg_hold_time_bars | 2.2250 |
| exposure | 0.1457 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
