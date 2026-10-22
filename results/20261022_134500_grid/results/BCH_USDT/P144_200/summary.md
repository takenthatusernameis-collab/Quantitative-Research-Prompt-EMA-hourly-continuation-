# EMA Hourly Continuation — BCH/USDT P144_200

**Symbol:** BCH/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 386 |
| net_profit_factor | 0.5398 |
| net_win_rate | 0.4896 |
| gross_profit_factor | 1.1187 |
| gross_win_rate | 0.5181 |
| sharpe_ratio | -4.2138 |
| sortino_ratio | -1.1699 |
| max_drawdown | 0.7699 |
| cagr | -0.4366 |
| net_avg_win | 47.3697 |
| net_avg_loss | -84.1891 |
| avg_hold_time_bars | 4.3135 |
| exposure | 0.0757 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
