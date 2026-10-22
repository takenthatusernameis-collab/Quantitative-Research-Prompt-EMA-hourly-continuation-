# EMA Hourly Continuation — SNX/USDT P55_89

**Symbol:** SNX/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 672 |
| net_profit_factor | 0.5717 |
| net_win_rate | 0.4866 |
| gross_profit_factor | 1.0821 |
| gross_win_rate | 0.5045 |
| sharpe_ratio | -5.1591 |
| sortino_ratio | -1.8743 |
| max_drawdown | 0.9057 |
| cagr | -0.6053 |
| net_avg_win | 36.9043 |
| net_avg_loss | -61.1858 |
| avg_hold_time_bars | 3.7798 |
| exposure | 0.1149 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
