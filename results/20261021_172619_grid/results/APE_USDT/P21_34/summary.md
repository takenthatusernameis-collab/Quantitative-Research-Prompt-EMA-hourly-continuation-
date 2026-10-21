# EMA Hourly Continuation — APE/USDT P21_34

**Symbol:** APE/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 274 |
| net_profit_factor | 0.6843 |
| net_win_rate | 0.4891 |
| gross_profit_factor | 0.9445 |
| gross_win_rate | 0.4891 |
| sharpe_ratio | -1.9144 |
| sortino_ratio | -0.4542 |
| max_drawdown | 0.4429 |
| cagr | -0.1881 |
| net_avg_win | 65.9164 |
| net_avg_loss | -92.1975 |
| avg_hold_time_bars | 4.1642 |
| exposure | 0.0519 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
