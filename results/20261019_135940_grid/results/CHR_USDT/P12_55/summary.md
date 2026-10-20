# EMA Hourly Continuation — CHR/USDT P12_55

**Symbol:** CHR/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1022 |
| net_profit_factor | 0.4980 |
| net_win_rate | 0.4325 |
| gross_profit_factor | 0.8352 |
| gross_win_rate | 0.4481 |
| sharpe_ratio | -6.9392 |
| sortino_ratio | -3.0969 |
| max_drawdown | 0.9788 |
| cagr | -0.7798 |
| net_avg_win | 21.9520 |
| net_avg_loss | -33.5911 |
| avg_hold_time_bars | 8.2632 |
| exposure | 0.3821 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
