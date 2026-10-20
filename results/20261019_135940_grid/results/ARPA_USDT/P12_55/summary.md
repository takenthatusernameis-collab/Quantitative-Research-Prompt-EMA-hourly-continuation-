# EMA Hourly Continuation — ARPA/USDT P12_55

**Symbol:** ARPA/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1099 |
| net_profit_factor | 0.5553 |
| net_win_rate | 0.4404 |
| gross_profit_factor | 0.9152 |
| gross_win_rate | 0.4586 |
| sharpe_ratio | -7.5439 |
| sortino_ratio | -3.5094 |
| max_drawdown | 0.9878 |
| cagr | -0.8190 |
| net_avg_win | 25.4586 |
| net_avg_loss | -36.0779 |
| avg_hold_time_bars | 7.8744 |
| exposure | 0.3916 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
