# EMA Hourly Continuation — CFG/USDT P8_21

**Symbol:** CFG/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1742 |
| net_profit_factor | 0.3159 |
| net_win_rate | 0.4041 |
| gross_profit_factor | 0.6649 |
| gross_win_rate | 0.4162 |
| sharpe_ratio | -12.0766 |
| sortino_ratio | -7.0996 |
| max_drawdown | 0.9999 |
| cagr | -0.9700 |
| net_avg_win | 6.5579 |
| net_avg_loss | -14.0802 |
| avg_hold_time_bars | 2.9162 |
| exposure | 0.2309 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
